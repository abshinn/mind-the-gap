#!/usr/bin/env python2.7 -B
"""get California census by district"""

import os
import pandas as pd
import pdb


def districts(lea_ids=[], columns=[], drop_columns=[], filename=""):
    """
    INPUT: pandas series of local education agency ids (optional)
    OUTPUT: pandas dataframe of census data with index as given series of LEA ids

    by default grab California census-by-district data 
    """

    if filename:
        print "[grabbing census data from: {}]".format(filename.split("_")[3])
    else:
        print "[grab California census data...]"
        filename = "../data/district/SDDS_School_Districts_California_Jul-17-2014.csv"

    censusdf = pd.read_csv(filename, na_values=['null'])
    censusdf.index = censusdf.pop("NCES ID")

    if columns:
        censusdf = censusdf[columns]

    if drop_columns:
        censusdf = censusdf.drop(drop_columns)

    if type(lea_ids) == pd.core.series.Series:
        return censusdf.loc[LEA_id]
    else:
        return censusdf


def all_districts(columns=[], census_path="../data/census/"):
    csvs = os.listdir(census_path)

    state_dfs = []
    for csv in csvs:
        state_dfs.append(districts(filename=(census_path + csv)))

    states = pd.concat(state_dfs, axis=0)

    if columns:
        states = states[columns]

    return states


if __name__ == "__main__":
    all_districts()
