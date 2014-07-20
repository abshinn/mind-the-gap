#!/usr/bin/env python2.7 
"""get DonorsChoose project data""" 

import pandas as pd
import numpy as np


def schools(state = "CA", year = 2011):
    """
    INPUT: kwargs state and year
    OUTPUT: pandas dataframe

    grab DonorsChoose Project data and return dataframe of schools
    """ 
    print "[grab DonorsChoose project data...]"

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
    statedf = df[df.state == state].copy()

    # free from memory 
    del df

    # sort df by schools, custom aggregate on projects
    schools = statedf.groupby("_NCESid").agg({'_projectid': pd.Series.nunique,
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

def school_lookup(schoolname):
    pass

