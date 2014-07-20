#!/usr/bin/env python2.7 -B
"""explore area/school/district recommendation using California as a subset"""

import pandas as pd
import numpy as np
import pdb

import similarity
import get_donorschoose
import get_nces
import get_census


def merge_NCES(school_ids):
    """
    INPUT: pandas series of NCES school ids
    OUTPUT: pandas dataframe with index as the given series of school ids

    grab NCES school information and NCES district finance data
    """
    print "[grab NCES data...]"

    columns = ["SCHNAM", "SURVYEAR", "LEAID", "FTE", "TOTFRL", "MEMBER", "ST_ratio"]
    NCES_schools = get_nces.schools(school_ids, columns=columns)

    columns = ["TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    NCES_districts = get_nces.districts(NCES_schools.LEAID, columns=columns)

    NCESdf = pd.concat([NCES_schools, NCES_districts], axis=1)

    return NCESdf


def combine_data():
    """
    INPUT: None
    OUTPUT: pandas dataframe

    combine DonorsChoose, NCES, and census data
    """
    print "combine data..."

    schools = get_donorschoose.schools()
    NCES = merge_NCES(schools.index)

    data = pd.concat([schools, NCES], axis = 1)
    n_records = len(data)

    # drop rows without local education agency (school district) id
    data = data.loc[data.LEAID.dropna().index]
    print "\tNaN indices: dropped {} schools".format(n_records - len(data))

    census = get_census.districts(data.LEAID)

    census = census.reset_index()
    del census["index"]
    census.index = data.index
   
    data = pd.concat([data, census], axis=1)

    return data


if __name__ == "__main__":
    data = combine_data()

    # prepare data for similarity calc
    data.drop(["SCHNAM", "District Name", "State"], axis=1, inplace=True)
    data[np.isnan(data)] = -1

    sim = similarity.cos(data)
