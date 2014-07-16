#!/usr/bin/env python
"""Pull pertinent data from NCES tab delimited files"""

import pandas as pd
import numpy as np
# import pdb


def NCES_boolean(x):
    if x == 1:
        return True
    elif x == 2:
        return False
    else:
        return np.nan


def get_NCES_schools(ids, columns=None):
    """step through NCES CCD school data and grab school stats for every Donors Choose NCESid"""

    # hard-code boolean columns
    boolcolumns = ["STATUS", "TYPE", "RECONSTF", "CHARTR", "MAGNET", "TITLEI", "STITLI"]

    # load-in NCES school data
    schooldf = pd.read_csv("data/school/sc111a_supp.txt", sep='\t', low_memory=False,
                           na_values=[-1, -2, -9, 'M', 'N'])

    schooldf.index = schooldf.pop("NCESSCH")

    if columns:
        outdf = schooldf[columns].loc[ids].copy()
        boolcolumns = [col for col in boolcolumns if col in columns]
    else:
        outdf = schooldf.loc[ids].copy()

    # free from memory
    # (this is step is probably unnecessary b/c it is already cleared from mem by exiting the namesapce)
    del schooldf

    for col in boolcolumns:
        outdf[col] = outdf[col].apply(NCES_boolean)

    return outdf


def get_NCES_states():
    pass

# def merge():
#     """output NCES school data for a given Donors Choose project data set"""
# 
#     columns = [u'essay_title', u'_projectid', u'date_completed', u'date_expired', u'funding_status', 
#                u'grade_level', u'num_donors', u'date_posted', u'poverty_level', u'students_reached', 
#                u'project_subject', u'subject_category', u'total_donations', u'tot_price_without_support', 
#                u'total_price_with_support', u'_schoolid', u'city', u'state', u'district', u'latitude', 
#                u'longitude', u'teach_for_america', u'_teacherid', u'zip', u'_NCESid', u'resource_type', u'county']
# 
#     df = pd.read_csv("data/looker_completed_projects_7_14_14.csv", skiprows=1, names=columns,
#                      parse_dates = ["date_posted", "date_completed", "date_expired"],
#                      true_values="Yes", false_values="No")
# 
#     DC_school_ids = df._NCESid.dropna().drop_duplicates().astype(np.int)
# 
#     NCESdf = get_NCES_data(DC_school_ids)
#     
#     pdb.set_trace()
# 
# 
# if __name__ == "__main__":
#     merge()
