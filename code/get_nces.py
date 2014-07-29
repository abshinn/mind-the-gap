#!/usr/bin/env python2.7  -B
"""pull pertinent data from NCES tab delimited files""" 

import pandas as pd
import numpy as np


def NCES_boolean(x):
    """convert nces non-standard boolean to True/False"""
    if x == 1:
        return True
    elif x == 2:
        return False
    else:
        return np.nan


def schools(_schoolids=None, columns=[], nonneg=False):
    """
    INPUT: pandas series of NCES school ids
           specific column names (optional)
    OUTPUT: pandas dataframe 

    step through NCES CCD school data and grab school stats for given Donors Choose NCES school id
    """

    na_values = ['M', 'N', 'R']

    if nonneg:
        na_values.extend([-1, -2, -9])

    # load-in NCES school data 
    schooldf = pd.read_csv("../data/school/sc111a_supp.txt", sep='\t', 
                           low_memory=False, na_values=na_values)

    schooldf.index = schooldf.pop("NCESSCH")

    schooldf["LEAID"] = schooldf["LEAID"].astype(np.int)

    # student-teacher ratio
    schooldf["ST_ratio"] = schooldf.MEMBER/schooldf.FTE

    if _schoolids != None:
        if columns:
            outdf = schooldf[columns].loc[_schoolids].copy()
        else:
            outdf = schooldf.loc[_schoolids].copy()
    else:
        if columns:
            outdf = schooldf[columns].copy()
        else:
            outdf = schooldf.copy()

    return outdf


def districts(lea_ids=[], columns=[], state="", dropna=False, nonneg=False, binarize=[]):
    """
    INPUT: pandas series of local education agency ids indexed by NCES school ids (optional)
           specific column names to include (optional)
    OUTPUT: pandas dataframe

    step through NCES CCD district data and grab school stats for every DonorsChoose NCES local education agency id
    """

    na_values = ['M', 'N', 'R']

    if nonneg:
        na_values.extend([-1, -2, -9])

    # load-in NCES school data
    districtdf = pd.read_csv("../data/district/sdf11_1a.txt", index_col=0, sep='\t',
                             low_memory=False, na_values=na_values)

    # make sure LEAIDs are integer values
    districtdf.index = districtdf.index.astype(np.int)

    districtinfo = pd.read_csv("../data/district/ag111a_supp.txt", index_col=1, sep='\t',
                             low_memory=False, na_values=na_values)

    info_columns = ["LATCOD", "LONCOD"]
    districtdf = pd.concat([districtdf, districtinfo[info_columns].loc[districtdf.index]], axis=1)
   
    if state:
        districtdf = districtdf[districtdf.STABBR == state] 

    for column in binarize:
       outdf = pd.concat([outdf, pd.get_dummies(districtdf[column], prefix=column)], axis=1)

    if type(lea_ids) == pd.core.series.Series:
        if columns:
            outdf = districtdf[columns].loc[lea_ids].copy()
        else:
            outdf = districtdf.loc[lea_ids].copy()

        outdf.index = lea_ids.index
    else:
        if columns:
            outdf = districtdf[columns].copy()
        else:
            outdf = districtdf.copy()

    if dropna:
        outdf = outdf.dropna()

    return outdf


def schools_and_districts(school_ids, nonneg=False):
    """
    INPUT: pandas series of NCES school ids
    OUTPUT: pandas dataframe with index as the given series of school ids

    grab both NCES school demographics and NCES district finance data
    """
    print "[grab NCES data...]"

    columns = ["SCHNAM", "SURVYEAR", "LEAID", "FTE", "TOTFRL", "MEMBER", "ST_ratio"]
    NCES_schools = schools(school_ids, columns=columns, nonneg=nonneg)

    columns = ["TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    NCES_districts = districts(NCES_schools.LEAID, columns=columns, nonneg=nonneg)

    NCESdf = pd.concat([NCES_schools, NCES_districts], axis=1)

    return NCESdf
