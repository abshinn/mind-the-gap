#!/usr/bin/env python2.7 -B
""" explore area/school/district recommendation using California as a subset """

import sys
sys.dont_write_bytecode = True

import pandas as pd
import numpy as np
import pdb

import merge


def grab_dcProjects(state = 'CA', year = 2011):
    """ grab DonorsChoose Project data and return dataframe of schools """ 
    print "[grab DonorsChoose data...]"

    # replace default column names with hard-coded short-names 
    columns = [u'essay_title', u'_projectid', u'date_completed', u'date_expired', u'funding_status', 
               u'grade_level', u'num_donors', u'date_posted', u'poverty_level', u'students_reached', 
               u'project_subject', u'subject_category', u'total_donations', u'tot_price_without_support', 
               u'total_price_with_support', u'_schoolid', u'city', u'state', u'district', u'latitude', 
               u'longitude', u'teach_for_america', u'_teacherid', u'zip', u'_NCESid', u'resource_type', u'county']

    df = pd.read_csv("../data/looker_completed_projects_7_14_14.csv", skiprows=1, names=columns,
                     parse_dates=["date_posted", "date_completed", "date_expired"], low_memory=False,
                     true_values="Yes", false_values="No")
    
    year_posted = df.date_posted.apply(lambda date: date.year)
    df["year_posted"] = year_posted

    df = df[df.year_posted == year]
    df2010 = df[df.state == state].copy()

    # free from memory 
    del df

    # sort df by schools, custom aggregate on projects
    schools = df2010.groupby("_NCESid").agg({'_projectid': pd.Series.nunique,
                                             'total_donations': np.sum,
                                             'students_reached': np.sum,
                                             'funding_status': lambda S: np.sum(S != 'expired')/np.float(len(S)),
                                             'poverty_level': lambda S: S.iloc[0], # only take one
                                             })

    # rename columns
    schools.columns = ['students_reached', 'projects', 'percent_funded', 'total_donations', 'poverty_level']

    # binarize poverty level
    binary_poverty = pd.get_dummies(schools.poverty_level)
    del schools['poverty_level']
    schools = pd.concat([schools, binary_poverty], axis=1)

    return schools


def grab_NCES(school_ids):
    """ grab NCES school information and NCES district finance data """
    print "[grab NCES data...]"

    NCES_schools = merge.get_NCES_schools(school_ids, columns=["SURVYEAR", "LEAID", "FTE", "TOTFRL", "MEMBER"])

    # student-teacher ratio
    NCES_schools["STratio"] = NCES_schools.MEMBER/NCES_schools.FTE

    # get NCES district revenue data                                                
    # note: there will be multiple entries for districts
#     NCES_districts = merge.get_NCES_districts(NCES_schools.LEAID, 
#                                               columns=["TOTALREV", "TFEDREV", 
#                                                        "TSTREV", "TLOCREV", 
#                                                        "TOTALEXP", "TCURSSVC",
#                                                        "TCAPOUT",
#                                                        "HR1", "HE1", "HE2",
#                                                        ])
 

#     NCESdf = pd.concat([NCES_schools, NCES_districts], axis=1)
    NCESdf = NCES_schools

    return NCESdf


def grab_census(LEA_id, columns=None):
    """ grab California census-by-district data """
    print "[grab California census data...]"

    censusdf = pd.read_csv("../data/district/SDDS_School_Districts_California_Jul-17-2014.csv")
    censusdf.index = censusdf.pop("NCES ID")

    return censusdf.loc[LEA_id]


def combine_data():
    """ combine DonorsChoose, NCES, and census data """
    print "merging data..."

    projects = grab_dcProjects()
    NCES = grab_NCES(projects.index)

    data = pd.concat([projects, NCES], axis = 1)
    n_records = len(data)

    # drop rows without local education agency (school district) id
    data = data.loc[data.LEAID.dropna().index]
    print "NaN indices: dropped {} schools".format(n_records - len(data))

    census = grab_census(data.LEAID)

    census = census.reset_index()
    census.index = data.index
    # delete a few columns?
   
    data = pd.concat([data, census], axis=1)

    return data


if __name__ == "__main__":
    combine_data()
