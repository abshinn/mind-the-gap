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


def potential():
    pass


if __name__ == "__main__":
    data = data_prep()
    pdb.set_trace()
    sim = similarity.simSchools(data, ref_columns=["District Name", "State"])
    pdb.set_trace()
