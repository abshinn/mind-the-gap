#!/usr/bin/env python2.7 
"""pull pertinent data from NCES tab delimited files""" 

import pandas as pd
import numpy as np


def NCES_boolean(x):
    if x == 1:
        return True
    elif x == 2:
        return False
    else:
        return np.nan


def schools(_schoolids, columns=None):
    """
    INPUT: pandas series of NCES school ids
           specific column names (optional)
    OUTPUT: pandas dataframe 

    step through NCES CCD school data and grab school stats for given Donors Choose NCES school id
    """

    # hard-code boolean columns
    boolcolumns = ["STATUS", "TYPE", "RECONSTF", "CHARTR", "MAGNET", "TITLEI", "STITLI"]

    # load-in NCES school data 
    schooldf = pd.read_csv("../data/school/sc111a_supp.txt", sep='\t', 
                           low_memory=False,
                           na_values=[-1, -2, -9, 'M', 'N'])

    schooldf.index = schooldf.pop("NCESSCH")

    # student-teacher ratio
    schooldf["ST_ratio"] = schooldf.MEMBER/schooldf.FTE

    for column in boolcolumns:
        schooldf[column] = schooldf[column].apply(NCES_boolean)

    if columns:
        outdf = schooldf[columns].loc[_schoolids].copy()
    else:
        outdf = schooldf.loc[_schoolids].copy()

    return outdf


def districts(lea_ids, columns=None):
    """
    INPUT: pandas series of local education agency ids indexed by NCES school ids
           specific column names to include (optional)
    OUTPUT: pandas dataframe

    step through NCES CCD district data and grab school stats for every DonorsChoose NCES local education agency id
    """

    # load-in NCES school data
    districtdf = pd.read_csv("../data/district/sdf11_1a.txt", index_col=0, sep='\t',
                             low_memory=False, na_values=[-1, -2, -9, 'M', 'N'])


    # make sure LEAIDs are integer values
    districtdf.index = districtdf.index.astype(np.int)

    if columns:
        outdf = districtdf[columns].loc[lea_ids].copy()
    else:
        outdf = districtdf.loc[lea_ids].copy()

    # index by school_ids instead of lea_ids
    outdf.index = lea_ids.index

    return outdf
