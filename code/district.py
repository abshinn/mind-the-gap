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
import feature_importance


def bash(command):
    """bash wrapper for calling topojson"""
    print "$ " + command
    p = subprocess.Popen(command.split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, errors = p.communicate()
    if output:
        print output
    if errors:
        print errors


def to_geojson(rec_df, basename="districts"):
    """Write recommendation dataframe to geojson.

    INPUT: pandas dataframe
    OUTPUT: written to pwd: basename.topo.json, basename.json
    """

    features = []
    for leaid in rec_df.index.values:
        point = geojson.Point((rec_df["LONCOD"].loc[leaid], rec_df["LATCOD"].loc[leaid]))
        properties = { "name": rec_df["District Name"].loc[leaid], 
                      "state": rec_df.STNAME.loc[leaid],
                         "ST": rec_df.State.loc[leaid],
                      "leaid": leaid,
                      "score": rec_df.score.loc[leaid],
                       "info": rec_df["info"].loc[leaid],
                      }
        features.append(geojson.Feature(geometry=point, properties=properties, id=leaid))

    collection = geojson.FeatureCollection(features) 

    with open(basename+".json", "w") as geo:
        geo.write(geojson.dumps(collection))

    bash("topojson -p -o {0}.topo.json {0}.json".format(basename))


def feature_selection(activity_threshold=3):
    """Train classifier on DonorsChoose set given a label to choose most important features.

    INPUT:
    OUTPUT: list of most important columns
    """

    dc_districts = get_donorschoose.districts()
    dc_index = dc_districts.index

    census = get_census.all_states()
    census = census.loc[dc_index].copy()

    columns = ["STNAME", "LATCOD", "LONCOD", "TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    data = pd.concat([census, nces.loc[census.index]], axis=1)

    label = dc_districts.activity > activity_threshold
#     feature_importance.importance()

    return ddf



def district_similarity():
    """Compute district similarity matrix using census, NCES, and census district data.

    OUTPUT: Similarity object
    """

    census = get_census.all_states()

    columns = ["STNAME", "LATCOD", "LONCOD", "TOTALREV", "TFEDREV", "TSTREV", "TLOCREV", "TOTALEXP", "TCURSSVC", "TCAPOUT", "HR1", "HE1", "HE2"]
    nces = get_nces.districts(columns=columns, nonneg=True)

    ddf = pd.concat([census, nces.loc[census.index]], axis=1)

    sim = similarity.Similarity(ddf, ref_columns=["District Name", "State", "STNAME", "LATCOD", "LONCOD"])

    return sim


def potential_districts(sim, n_potential=15, activity_threshold=3):
    """Find potentially active districts outside of DonorsChoose network.

    OUTPUT: pandas dataframe of recommended distrcits
            districts.topo.json
            district.json
    """

    dc_districts = get_donorschoose.districts()

    active_districts = set(dc_districts[dc_districts.activity > activity_threshold].index.values.astype(np.int))
    all_districts = set(sim.data.index.values.astype(np.int))

    potential = all_districts - (active_districts & all_districts)

    rms = sim.rms_score(potential, active_districts, normalize=True)
     
    # potential districts most similar to active districts in descending order
    potential_df = pd.DataFrame(sorted(zip(potential, rms), key=lambda (x, y): y, reverse=True))
    potential_df.columns = ["leaid", "score"]
    potential_df.index = potential_df.pop("leaid")
    potential_df["State"] = sim.data["State"].loc[potential_df.index]

    # pick at most n_potential recommendations for each state
    recommend = []
    for state in sim.data.State.value_counts().index:
        recommend.extend(potential_df[potential_df.State == state].head(n_potential).index.values)


    rec_df = sim.data[["District Name", "STNAME", "State", "LATCOD", "LONCOD"]].loc[recommend]
    rec_df["score"] = potential_df.score.loc[recommend]

    N_rec = len(rec_df)
    rec_df.dropna(inplace=True)
    print "NaNs: drop {} districts".format(N_rec - len(rec_df))
 
    # build tooltip
    district_info = []
    for leaid in rec_df.index:
        tooltip = []
        tooltip.append( "{}".format(rec_df.loc[leaid, "District Name"]) )
        tooltip.append( "students: {}".format(sim.data.loc[leaid, "Total Students"].astype(np.int)) )
        tooltip.append("")
        
        most_sim = sim.most_similar(leaid)
        most_sim.drop(leaid)
        most_sim = most_sim.loc[filter(lambda leaid: True if leaid in active_districts else False, most_sim.index)]
        closest = most_sim.head(1).index[0]
        
#         same, close = sim.closest_features([leaid, closest])
#         closest_features = list(same) + list(close)
        
        tooltip.append( "Most similar to {}, {}".format(most_sim.loc[closest, "District Name"], most_sim.loc[closest, "State"]) )
#         tooltip.append( "(based on: {}, {})".format(closest_features[0], closest_features[1]) )
        
        tooltip.append( "students: {}".format(sim.data.loc[closest, "Total Students"].astype(np.int)) )
        tooltip.append( "projects: {}".format(dc_districts.loc[closest, "projects"].astype(np.int)) )
        donation_per_project = dc_districts.loc[closest, "total_donations"] / dc_districts.loc[closest, "projects"]
        tooltip.append( "received donations/project: ${:.2f}".format(donation_per_project) )
        htmltooltip = "<br/>".join(tooltip) 
        district_info.append(htmltooltip)

    info_series = pd.Series(district_info)
    info_series.index = rec_df.index
    rec_df["info"] = info_series

    to_geojson(rec_df)

    return rec_df
       

if __name__ == "__main__":
    sim = district_similarity()
    rec_df = potential_districts(sim)
