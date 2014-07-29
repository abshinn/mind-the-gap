#!/usr/bin/env python2.7 -B
"""compute district similarity for all schools in US"""

import pandas as pd
import numpy as np
import pdb

import similarity
import get_donorschoose
import get_nces
import get_census
import geojson
import subprocess


def bash(command):
    """bash wrapper for calling topojson"""
    print "$ " + command
    p = subprocess.Popen(command.split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, errors = p.communicate()
    if output:
        print output
    if errors:
        print errors


def district_similarity():
    """Compute district similarity matrix using census, NCES, and census district data.

    OUTPUT: Similarity object
            pickled Similarity object (optional)
    """

    census = get_census.all_states()

    columns = ["STNAME", "LATCOD", "LONCOD", "TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    ddf = pd.concat([census, nces.loc[census.index]], axis=1)

    sim = similarity.Similarity(ddf, ref_columns=["District Name", "State", "STNAME", "LATCOD", "LONCOD"])

    return sim


def potential_districts(sim, n_potential=15, activity_threshold=3):
    """Find potentially active districts outside of DonorsChoose network.

    OUTPUT: topojson with recommended school districts 
    """

    dc_districts = get_donorschoose.districts()

    active_districts = set(dc_districts[dc_districts.activity > activity_threshold].index.values.astype(np.int))
    all_districts = set(sim.data.index.values.astype(np.int))

    potential = all_districts - (active_districts & all_districts)

    rms = sim.rms_score(potential, active_districts, normalize=True)
     
    # sorted potential districts
    potential_df = pd.DataFrame(sorted(zip(potential, norm_rms), key=lambda (x, y): y, reverse=True))
    potential_df.columns = ["leaid", "score"]
    potential_df.index = potential_df.pop("leaid")
    potential_df["State"] = sim.data["State"].loc[potential_df.index]

    # pick at most n_potential recommendations for each state
    recommend = []
    for state in sim.data.State.value_counts().index:
        recommend.extend(potential_df[potential_df.State == state].head(n_potential).index.values)

    # active DonorsChoose schools recieved $x in donations with an average of y projects
#     for r in recommend:
#         most_sim_nces = sim.most_similar(r, in_group=most_active, n=10)
#         most_sim = dc_districts.loc[most_sim_nces.index]
#         break
# 
#     if True:
#         return r, most_sim_nces, most_sim, most_active
    # sim.data where the rows are the most similar schools in decreasing order

    rec_df = sim.data[["District Name", "STNAME", "State", "LATCOD", "LONCOD"]].loc[recommend]
    rec_df["score"] = potential_df.score.loc[recommend]

    N_rec = len(rec_df)
    rec_df.dropna(inplace=True)
    print "NaNs: drop {} districts".format(N_rec- len(rec_df))
   
    to_geojson(rec_df)

    return rec_df
       

def to_geojson(rec_df, basename="districts"):
    """Write recommendation dataframe to geojson.

    INPUT: pandas dataframe
    OUTPUT: written to pwd: basename.topo.json, basename.json
    """

    features = []
    for leaid in rec_df.index.values:
        point = geojson.Point((rec["LONCOD"].loc[leaid], rec_df["LATCOD"].loc[leaid]))
        properties = { "name": rec_df["District Name"].loc[leaid], 
                      "state": rec_df.STNAME.loc[leaid],
                         "ST": rec_df.State.loc[leaid],
                      "leaid": leaid,
                      "score": ref_df.score.loc[leaid],
                      }
        features.append(geojson.Feature(geometry=point, properties=properties, id=leaid))

    collection = geojson.FeatureCollection(features) 

    with open(basename+".json", "w") as geo:
        geo.write(geojson.dumps(collection))

    bash("topojson -p -o {0}.topo.json {0}.json".format(basename))


if __name__ == "__main__":
    sim = district_similarity()
    rec_df = potential_districts(sim)
