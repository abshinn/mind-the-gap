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

#     dc_districts = get_donorschoose.districts(year=2011)
    dc_districts = get_donorschoose.districts()

    all_dc = dc_districts.index
    most_active = set(dc_districts[dc_districts.projects >= 10].index.values.astype(np.int))
    all_districts = set(sim.data.index.values.astype(np.int))
    potential = all_districts - (most_active & all_districts)

    rms = sim.rms_score(potential, most_active)
    
    # list of sorted potential districts
    p = sorted(zip(potential, rms), key=lambda (x, y): y, reverse=True)
    pdf = pd.DataFrame(p)
    pdf.columns = ["leaid", "score"]
    pdf.index = pdf.pop("leaid")
    recommend = pdf.index[:500]

    # warning: renaming of df
#     most_active = sim.data[["District Name", "STNAME", "LATCOD", "LONCOD"]].loc[most_active.index]
    rec = sim.data[["District Name", "STNAME", "LATCOD", "LONCOD"]].loc[recommend]
#     lenma = len(most_active)
#     most_active.dropna(inplace=True)
#     print "NaNs: dropped {} districts".format(lenma - len(most_active))
    lenrec = len(rec)
    rec.dropna(inplace=True)
    print "NaNs: dropped {} districts".format(lenrec - len(rec))

    features = []
    for leaid in rec.index.values:
        point = geojson.Point((rec["LONCOD"].loc[leaid], rec["LATCOD"].loc[leaid]))
        properties = {"name" : rec["District Name"].loc[leaid], 
                      "state": rec["STNAME"].loc[leaid],
                      "leaid": leaid,
                      "score": str(pdf.loc[leaid]),
                      }
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
