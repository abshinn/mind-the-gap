""" calculate distance-similarity """

import pandas as pd
import numpy as np

from scipy.spatial.distance import cosine


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
    data = dataframe.values

    # base similarity matrix (all dot products)
    # replace this with A.dot(A.T).todense() for sparse representation
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

    def __init__(self, data, ref_columns):
        data["ref"] = np.arange( len(data) )
        ref_columns.append("ref")
        self.data = data
      
        calcdata = data.drop(ref_columns, axis=1)._get_numeric_data()
        calcdata[np.isnan(calcdata)] = -1 # try keeping the NaNs at some point
        self.sim = matmultcos( calcdata )

    def lookup_index(self, nces_id):
        return self.data.loc[nces_id].ref

    def most_similar(self, nces_id, n=10):
        most_sim_index = np.argsort(self.sim[self.lookup_index(nces_id),1:n+1])
        return self.data.iloc[most_sim_index]

    def __str__(self):
        return "similarity matrix of shape: {}".format(self.sim.shape)
