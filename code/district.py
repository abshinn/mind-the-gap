#!/usr/bin/env python2.7 -B
"""compute district similarity for all schools in US"""

import pandas as pd
import numpy as np
import pdb

import similarity
import get_donorschoose
import get_nces
import get_census
import pickle


def district_similarity(pkle=False):
    """Compute district similarity matrix using census, NCES, and census district data.

    OUTPUT: Similarity object
    """
    print "combine DonorsChoose, NCES, and Census data..."

    census = get_census.all_districts()

    columns = ["TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    ddf = pd.concat([census, nces.loc[census.index]], axis=1)

    sim = similarity.Similarity(data, ref_columns=["District Name", "State"])

    if pkle:
        pickle.dump(sim, "district_similarity.pkle")

    return sim


def potential_districts():
    """Find potentially active districts outside of DonorsChoose network.

    OUTPUT:
    """

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

    # pseudo
    # reduce dcdistricts down to most active
    # compile list of potential districts
    # compute similarity
    # compute activity metric
    # save into csv

    return dcdistricts
       

if __name__ == "__main__":
    district_similarity(pkle=True) 
#     potential_districts()
