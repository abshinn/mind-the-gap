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
import geojson


def district_similarity(pkle=False):
    """Compute district similarity matrix using census, NCES, and census district data.

    OUTPUT: Similarity object
            pickled Similarity object (optional)
    """

    census = get_census.all_states()

    columns = ["STNAME", "TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    ddf = pd.concat([census, nces.loc[census.index]], axis=1)

    sim = similarity.Similarity(ddf, ref_columns=["District Name", "State", "STNAME"])

    if pkle:
        with open("district_similarity.pkle", "wb") as p:
            pickle.dump(sim, p)

    return sim


def potential_districts():
    """Find potentially active districts outside of DonorsChoose network.

    OUTPUT:
    """

    dc_districts = get_donorschoose.districts(year=2011)

    all_dc = dc_districts.index
    most_active = dc_districts.projects[dc_districts.projects >= 100].index
    # pseudo
    # reduce dcdistricts down to most active
    # compile list of potential districts
    # compute similarity
    # compute activity metric
    # save into csv

    return dc_districts
       

if __name__ == "__main__":
    sim = district_similarity() 
    ddf = potential_districts()
    most_active = ddf.projects[ddf.projects >= 100].index
    all_dc = ddf.index
    ma = ddf.loc[most_active]
    names = sim.data[["District Name", "STNAME"]].loc[ma.index]
    ma = pd.concat([ma, names], axis=1)
    ma = ma.dropna()
    features = []
    for leaid in ma.index.values.astype(np.int):
        point = geojson.Point((ma.loc[leaid].longitude, ma.loc[leaid].latitude))
        properties = {"name" : ma["District Name"].loc[leaid], "state": ma["STNAME"].loc[leaid]}
        features.append(geojson.Feature(geometry=point, properties=properties))#, id=leaid))
    collection = geojson.FeatureCollection(features) 
    with open("test.json", "w") as geo:
        geo.write(geojson.dumps(collection))
