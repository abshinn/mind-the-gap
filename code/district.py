#!/usr/bin/env python2.7 -B
"""compute district similarity for all schools in US"""

import pandas as pd
import numpy as np

import similarity
import get_donorschoose
import get_nces
import get_census


def data_prep():
    """Combine DonorsChoose, NCES, and census data for some data crunching.

    OUTPUT: pandas dataframe
    """
    print "combine DonorsChoose, NCES, and Census data..."

    schools = get_donorschoose.schools(state="CA", year=2011)
    NCES = get_nces.schools_and_districts(schools.index, nonneg=True)

    data = pd.concat([schools, NCES], axis=1)
    n_records = len(data)

    # drop rows without local education agency (school district) id
    data = data.loc[data.LEAID.dropna().index]
    print "\tNaN indices: dropped {} schools".format(n_records - len(data))

    census = get_census.districts(data.LEAID)

    census = census.reset_index()
    census.drop(["index"], axis=1, inplace=True)
    census.index = data.index
   
    data = pd.concat([data, census], axis=1)

    # note: non-numeric columns are automatically dropped before any calculation within simSchools
#     data.drop(["SURVYEAR", "LEAID"], axis=1, inplace=True)

#    data[np.isnan(data)] = -1

    return data 


def potential():
    pass


if __name__ == "__main__":
    data = data_prep()
    sim = similarity.simSchools(data, ref_columns=["SCHNAM", "District Name", "State"])
