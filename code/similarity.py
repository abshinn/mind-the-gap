""" calculate distance-similarity """

import pandas as pd
import numpy as np
import datetime as dt

from scipy.spatial.distance import cosine
from sklearn.preprocessing import normalize


def cos(dataframe):
    """
    INPUT: pandas dataframe
    OUTPUT: numpy square ndarray

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
    OUTPUT: numpy square ndarray

    matrix multiplcation version of cosine similarity
    """

#     data = normalize(dataframe.values)
    data = (dataframe.values - dataframe.values.mean(axis=0))/dataframe.values.std(axis=0)

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


class simSchools(object):
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
#         calcdata[np.isnan(calcdata)] = -1 # try keeping the NaNs at some point
        self.numeric_data = calcdata
        self.sim = matmultcos( calcdata )

    def closest_features(self, nces_ids):
        """Given two school ids, determine the features that are most similar.
        INPUT: list of two nces_ids of schools to compare closeness
        OUTPUT: tuple
                 same -- list of columns which are the same
                close -- list of tuples of columns and their respective arbirtrary column-similarity metric
        """
        data = self.numeric_data
        norm = data/data.std(axis=0)
        diff = (norm.loc[nces_ids[0]] - norm.loc[nces_ids[1]]).abs()
        same = data.columns[diff.values == 0].values
        diff = diff.dropna()
        close = sorted(zip(diff.index, diff), key=lambda (col, sim): sim)
        close = filter(lambda (col, sim): sim, close)
        return same, close

    def lookup_index(self, nces_id):
        return self.data.loc[nces_id].ref

    def most_similar(self, nces_id, n=None):
        most_sim_index = np.argsort(self.sim[self.lookup_index(nces_id),:])[0:n]
#         print np.sort(self.sim[self.lookup_index(nces_id),:])[0:n]
        return self.data.iloc[most_sim_index]

    def __str__(self):
        return "similarity matrix of shape: {}".format(self.sim.shape)
