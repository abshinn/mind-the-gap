""" calculate distance-similarity """

import sys
sys.dont_write_bytecode = True

import pandas as pd
import numpy as np
# import pdb

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

    for i in xrange(m):
        for j in xrange(m):
            if i != j:
                mat[i][j] = cosine(data[i,:], data[j,:])
            else:
                mat[i][j] = 0.
    return mat
