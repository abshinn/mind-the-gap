#!/usr/bin/env python2.7 -B
"""compute district similarity for all schools in US"""

import pandas as pd
import numpy as np
import pdb

import similarity
import get_donorschoose
import get_nces
import get_census


def data_prep():
    """Combine census and NCES and census district data for a similarity calculation.

    OUTPUT: pandas dataframe
    """
    print "combine DonorsChoose, NCES, and Census data..."

    census = get_census.all_districts()

    columns = ["TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    ddf = pd.concat([census, nces.loc[census.index]], axis=1)

    return ddf


def potential_districts():
#     data = data_prep()
#     sim = similarity.simSchools(data, ref_columns=["District Name", "State"])

    schools = get_donorschoose.schools(year=2011)
    schools = pd.concat([ schools, get_nces.schools(schools.index, columns=["LEAID", "FTE", "MEMBER", "ST_ratio", "TOTFRL"]) ], axis=1)

    dcdistricts = schools.groupby("LEAID").agg({"students_reached": np.sum,
                                                "projects": np.sum,
                                                "percent_funded": np.mean,
                                                "total_donations": np.sum,
                                                "high poverty": np.sum,
                                                "highest poverty": np.sum,
                                                "low poverty": np.sum,
                                                "FTE": np.mean,
                                                "TOTFRL": np.sum,
                                                "MEMBER": np.sum,
                                                "ST_ratio": np.mean,
                                               }).sort("projects", ascending=False)
    return dcdistricts
       


if __name__ == "__main__":
    potential_districts()
