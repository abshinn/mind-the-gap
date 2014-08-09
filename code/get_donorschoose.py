#!/usr/bin/env python2.7 -B
"""get_donorschoose.py

   Obtain DonorsChoose project data from their Looker tool:
      ../data/looker_completed_projects_7_14_14.csv

   Access is available upon request from:
      http://data.donorschoose.org/open-data-unleashed/

   DonorsChoose.org data is licensed under a Creative Commons Attribution-NonCommercial license:
      http://creativecommons.org/licenses/by-nc/3.0/
""" 

import pandas as pd
import numpy as np
import get_nces

def schools(state="", year=None):
    """
    INPUT: optional kwargs state [str] and year (posted) [int]
    OUTPUT: pandas dataframe

    grab DonorsChoose Project data and return dataframe of schools
    """ 
    print "[grab DonorsChoose project data...]"

    # replace default column names with hard-coded short-names 
    columns = [u"essay_title", u"_projectid", u"date_completed", u"date_expired", u"funding_status", 
               u"grade_level", u"num_donors", u"date_posted", u"poverty_level", u"students_reached", 
               u"project_subject", u"subject_category", u"total_donations", u"tot_price_without_support", 
               u"total_price_with_support", u"_schoolid", u"city", u"state", u"district", u"latitude", 
               u"longitude", u"teach_for_america", u"_teacherid", u"zip", u"_NCESid", u"resource_type", u"county"]

    df = pd.read_csv("../data/looker_completed_projects_7_14_14.csv", skiprows=1, names=columns,
                     parse_dates=["date_posted", "date_completed", "date_expired"], low_memory=False,
                     true_values="Yes", false_values="No")
    
    year_posted = df.date_posted.apply(lambda date: date.year)
    df["year_posted"] = year_posted

    if year:
        print "\tposted year: {}".format(year)
        df = df[df.year_posted == year]

    if state:
        print "\tstate: {}".format(state)
        df = df[df.state == state]

    dflen = len(df)
    df = df[np.isfinite(df._NCESid)]
    print "\tNo NCESid: {}/{} projects dropped".format(dflen - len(df), dflen)

    df._NCESid = df._NCESid.astype(np.int)

    # sort df by schools, custom aggregate on projects
    schools = df.groupby("_NCESid").agg({"_projectid": pd.Series.nunique,
                                         "year_posted": np.min,
                                         "total_donations": np.sum,
                                         "students_reached": np.sum,
                                         "funding_status": lambda S: np.sum(S != "expired")/np.float(len(S)),
                                         "poverty_level": lambda S: S.iloc[0], # only take one
                                         "latitude": lambda S: S.iloc[0],
                                         "longitude": lambda S: S.iloc[0],
                                         })

    print "\t{} schools".format(len(schools))

    # free from memory 
    del df

    # rename columns
    schools.columns = ["projects", "total_donations", "latitude", "percent_funded", "students_reached", "start_year", "poverty_level", "longitude"]

    # leave out 2014
    schools = schools[schools.start_year <= 2013]

    schools["years_active"] = 2014 - schools.start_year
    schools["activity"] = schools.projects.astype(np.float) / schools.years_active

    # binarize poverty level
    binary_poverty = pd.get_dummies(schools.poverty_level)
    del schools["poverty_level"]
    schools = pd.concat([schools, binary_poverty], axis=1)

    return schools


def districts(year=None):
    """Get DonorsChoose and NCES school data and group by districts.

    OUTPUT: pandas dataframe
    """

    dc_schools = schools(year=year)
    dc_schools = pd.concat([ dc_schools, get_nces.schools(dc_schools.index, columns=["LEAID", "FTE", "MEMBER", "ST_ratio", "TOTFRL"]) ], axis=1)

    dc_districts = dc_schools.groupby("LEAID").agg({"students_reached": np.sum,
                                                    "projects": np.sum,
                                                    "years_active": np.min,
                                                    "activity": np.mean,
                                                    "percent_funded": np.mean,
                                                    "total_donations": np.sum,
                                                    "high poverty": np.sum,
                                                    "highest poverty": np.sum,
                                                    "low poverty": np.sum,
                                                    "FTE": np.mean,
                                                    "TOTFRL": np.sum,
                                                    "MEMBER": np.sum,
                                                    "ST_ratio": np.mean,
                                                    "latitude": np.mean,
                                                    "longitude": np.mean,
                                                   }).sort("projects", ascending=False)

    return dc_districts
