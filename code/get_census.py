#!/usr/bin/env python2.7
"""get California census by district"""

import pandas as pd


def districts(LEA_id, columns=None):
    """
    INPUT: pandas series of local education agency ids
    OUTPUT: pandas dataframe of census data with index as given series of LEA ids

    grab California census-by-district data
    """
    print "[grab California census data...]"

    censusdf = pd.read_csv("../data/district/SDDS_School_Districts_California_Jul-17-2014.csv", na_values=['null'])
    censusdf.index = censusdf.pop("NCES ID")

    if columns:
        censusdf = censusdf[columns]

    return censusdf.loc[LEA_id]
