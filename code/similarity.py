"""calculate distance-similarity"""

import pandas as pd
import numpy as np
import pdb

from scipy.spatial.distance import cosine


def cos(dataframe):
    """
    INPUT: pandas dataframe
    OUTPUT: numpy square NDarray

    create a cosine similarity square matrix based on the rows of 'dataframe'
    """

    data = dataframe.values
    m, n = data.shape

    mat = np.zeros((m, m))

    # note: this is a diagonal matrix and can be optimized
    for i in xrange(m):
        for j in xrange(m):
            if i != j:
                mat[i][j] = cosine(data[i,:], data[j,:])
            else:
                mat[i][j] = 0.
    return mat


def matmultcos(dataframe):
    """
    INPUT: pandas dataframe
    OUTPUT: numpy square NDarray

    matrix multiplication version of cosine similarity
    """

    # normalize and force NaNs to be 0 (mean value) so it won't affect the similarity calculation
    data = (dataframe.values - dataframe.values.mean(axis=0))/dataframe.values.std(axis=0)
    data[np.isnan(data)] = 0.

    # base similarity matrix (all dot products)
    # replace this with data.dot(data.T).todense() if sparce
    similar = np.dot(data, data.T)
    
    # squared magnitude of preference vectors (number of occurrences)
    square_mag = np.diag(similar)
    
    # inverse squared magnitude
    inv_square_mag = 1. / square_mag
    
    # if it doesn't occur, set it's inverse magnitude to zero (instead of inf)
    inv_square_mag[np.isinf(inv_square_mag)] = 0.
    
    # inverse of the magnitude
    inv_mag = np.sqrt(inv_square_mag)
    
    # cosine similarity (elementwise multiply by inverse magnitudes)
    cos = similar * inv_mag
    cos = cos.T * inv_mag
    cos = 1. - cos

    return cos


class Similarity(object):
    """Compute and store cosine similarity matrix, allow methods to operate on the stored matrix.

    REQUIRED INPUT: 
           data -- pandas dataframe with all numeric columns except for reference columns
    ref_columns -- list of column names to use for reference
    """

    def __init__(self, data, ref_columns=[]):
        data["ref"] = np.arange( len(data))
        ref_columns.append("ref")
        self.data = data
      
        calcdata = data.drop(ref_columns, axis=1)._get_numeric_data()
        self.numeric_data = calcdata
        self.sim = matmultcos( calcdata )

    def closest_features(self, nces_ids):
        """Given two school ids, determine the features that are most similar.

        INPUT: list of two nces_ids of schools to compare closeness
        OUTPUT: tuple (same, close)
                 same -- list of columns which are the same
                close -- list of tuples of columns and their respective arbitrary column-similarity metric
        """
        data = self.numeric_data
        norm = data/data.std(axis=0)
        diff = (norm.loc[nces_ids[0]] - norm.loc[nces_ids[1]]).abs()
        same = data.columns[diff.values == 0].values
        diff = diff.dropna()
        close = sorted(zip(diff.index, diff), key=lambda (col, sim): sim)
        close = filter(lambda (col, sim): sim, close)
        close = [feature for feature, sim in close]
        return same, close

    def _lookup_index(self, nces_id):
        return self.data.loc[nces_id].ref

    def rms_score(self, group1, group2, normalize=False):
        """Metric with which to compare one group of items to another.

        INPUT: group1 -- pandas series of nces_ids
               group2 -- pandas series of nces_ids
        OUTPUT: rms score
        """
        v = self.sim[self._lookup_index(group1).dropna(), :]
        v = v[:, self._lookup_index(group2).dropna()]
        rms = np.sqrt(np.multiply(v,v).mean(axis=1))

        if normalize:
            return (100*rms/rms.max()).astype(np.int)
        else:
            return rms

    def most_similar(self, nces_id, n=None):
        most_sim_index = np.argsort(self.sim[self._lookup_index(nces_id),:])[0:n]
        return self.data.iloc[most_sim_index]

    def most_similar_in_group(self, nces_id, in_group, n=None):
        s = self.sim[self._lookup_index(nces_id), :]
        s = s[self._lookup_index(in_group).dropna()]

    def __str__(self):
        return "Similarity object of shape: {}".format(self.sim.shape)
