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
import subprocess


def bash(command):
    print "$ " + command
    p = subprocess.Popen(command.split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, errors = p.communicate()
    if output:
        print output
    if errors:
        print errors


def district_similarity(pkle=False):
    """Compute district similarity matrix using census, NCES, and census district data.

    OUTPUT: Similarity object
            pickled Similarity object (optional)
    """

    census = get_census.all_states()

    columns = ["STNAME", "LATCOD", "LONCOD", "TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    ddf = pd.concat([census, nces.loc[census.index]], axis=1)

    sim = similarity.Similarity(ddf, ref_columns=["District Name", "State", "STNAME", "LATCOD", "LONCOD"])

    if pkle:
        with open("district_similarity.pkle", "wb") as p:
            pickle.dump(sim, p)

    return sim


def potential_districts(sim):
    """Find potentially active districts outside of DonorsChoose network.

    OUTPUT:
    """

    dc_districts = get_donorschoose.districts(year=2011)

    all_dc = dc_districts.index
    most_active = set(dc_districts[dc_districts.projects >= 10].index.values.astype(np.int))
    all_districts = set(sim.data.index.values.astype(np.int))
    potential = all_districts - (most_active & all_districts)

    rms = sim.rms_score(potential, most_active)
    
    # list of sorted potential districts
    p = sorted(zip(potential, rms), key=lambda (x, y): y, reverse=True)

    if True:
        return rms

    # warning: renaming of df
    most_active = sim.data[["District Name", "STNAME", "LATCOD", "LONCOD"]].loc[most_active.index]
    lenma = len(most_active)
    most_active.dropna(inplace=True)
    print "NaNs: dropped {} districts".format(lenma - len(most_active))

    features = []
    for leaid in most_active.index.values.astype(np.int):
        point = geojson.Point((most_active["LONCOD"].loc[leaid], most_active["LATCOD"].loc[leaid]))
        properties = {"name" : most_active["District Name"].loc[leaid], "state": most_active["STNAME"].loc[leaid]}
        features.append(geojson.Feature(geometry=point, properties=properties))#, id=leaid))

    collection = geojson.FeatureCollection(features) 


    basename = "districts"
    with open(basename + ".json", "w") as geo:
        geo.write(geojson.dumps(collection))

    bash("topojson -p name -p state -o {} {}".format(basename + ".topo.json", basename + ".json"))
#     bash("mv *.json ../interactive/json/")

    # pseudo
    # reduce dcdistricts down to most active
    # compile list of potential districts
    # compute similarity
    # compute activity metric
    # save into csv

#     return dc_districts
       

if __name__ == "__main__":
    pass
