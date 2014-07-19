#!/usr/bin/env python2.7 -B
"""Pull pertinent data from NCES tab delimited files"""

import sys
sys.dont_write_bytecode = True

import pandas as pd
import numpy as np
# import pdb


def NCES_boolean(x):
    if x == 1:
        return True
    elif x == 2:
        return False
    else:
        return np.nan


def get_NCES_schools(_schoolids, columns=None):
    """step through NCES CCD school data and grab school stats for every Donors Choose NCES school id"""

    # hard-code boolean columns
    boolcolumns = ["STATUS", "TYPE", "RECONSTF", "CHARTR", "MAGNET", "TITLEI", "STITLI"]

    # load-in NCES school data
    schooldf = pd.read_csv("../data/school/sc111a_supp.txt", sep='\t', low_memory=False,
                           na_values=[-1, -2, -9, 'M', 'N'])

    schooldf.index = schooldf.pop("NCESSCH")

    if columns:
        outdf = schooldf[columns].loc[_schoolids].copy()
        boolcolumns = [col for col in boolcolumns if col in columns]
    else:
        outdf = schooldf.loc[_schoolids].copy()

    # free from memory
    # (this is step is probably unnecessary b/c it is already cleared from mem by exiting the namesapce)
    del schooldf

    for col in boolcolumns:
        outdf[col] = outdf[col].apply(NCES_boolean)

    return outdf


def get_NCES_districts(_LEAids, columns=None):
    """step through NCES CCD district data and grab school stats for every DonorsChoose NCES local education agency id (LEAid)"""

    # hard-code boolean columns
#     boolcolumns = ["STATUS", "TYPE", "RECONSTF", "CHARTR", "MAGNET", "TITLEI", "STITLI"]

    # load-in NCES school data
    districtdf = pd.read_csv("../data/district/sdf11_1a.txt", index_col=0, sep='\t',
                             low_memory=False, na_values=[-1, -2, -9, 'M', 'N'])


    # make sure LEAIDs are integer values
    districtdf.index = districtdf.index.astype(np.int)

    if columns:
        outdf = districtdf[columns].loc[_LEAids].copy()
    else:
        outdf = districtdf.loc[_LEAids].copy()

#     outdf = districtdf[columns].loc[_LEAids].copy()
    outdf.index = _LEAids.index

    return outdf
