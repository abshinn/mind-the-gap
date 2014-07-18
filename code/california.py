#!/usr/bin/env python2.7

import pandas as pd
import numpy as np
import pdb

import merge # user-defined

def combine_data(self):
    """ combine DonorsChoose project data, NCES district finance data, and census data """
    print "[combining data...]"

    # replace default column names with hard-coded short-names 
    columns = [u'essay_title', u'_projectid', u'date_completed', u'date_expired', u'funding_status', 
               u'grade_level', u'num_donors', u'date_posted', u'poverty_level', u'students_reached', 
               u'project_subject', u'subject_category', u'total_donations', u'tot_price_without_support', 
               u'total_price_with_support', u'_schoolid', u'city', u'state', u'district', u'latitude', 
               u'longitude', u'teach_for_america', u'_teacherid', u'zip', u'_NCESid', u'resource_type', u'county']

    df = pd.read_csv("../data/looker_completed_projects_7_14_14.csv", skiprows=1, names=columns,
                     parse_dates = ["date_posted", "date_completed", "date_expired"], low_memory=False,
                     true_values="Yes", false_values="No")

    year_posted = df.date_posted.apply(lambda date: date.year)
    df["year_posted"] = year_posted

    # only look at CA data from 2010
    df = df[df.year_posted == 2010]
    df2010 = df[df.state == 'CA'].copy()

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

    # get NCES school data, choose columns
    NCES_schools = merge.get_NCES_schools(schools.index, 
                                          columns=["SURVYEAR", "LEAID",
                                                   "FRELCH", "REDLCH",
                                                   "TOTFRL", 
#                                                    "FTE",
#                                                      "ULOCAL", 
#                                                      "STATUS", "TYPE",
#                                                      "RECONSTY", "RECONSTF", 
#                                                      "CHARTR", "MAGNET",
#                                                      "MAGNET",
#                                                      "TITLEI", "STITLI", 
#                                                    "MEMBER", "TOTETH", 
#                                                    "WHITE", "BLACK",
                                                    ])

    NCES_schools["STratio"] = NCES_schools.MEMBER/NCES_schools.FTE

    # turn student counts into percentages
    NCES_schools["WHITE"] = NCES_schools.WHITE.astype(np.float)/NCES_schools.MEMBER
    NCES_schools["BLACK"] = NCES_schools.BLACK.astype(np.float)/NCES_schools.MEMBER
    NCES_schools["ETHpercent"] = NCES_schools.TOTETH.astype(np.float)/NCES_schools.MEMBER

    # get NCES district finance data                                                
    # note: there will be multiple entries for districts
    NCES_districts = merge.get_NCES_districts(NCES_schools.LEAID, 
                                              columns=["TOTALREV", "TFEDREV", 
                                                       "TSTREV", "TLOCREV", 
                                                       "TOTALEXP", "TCURSSVC",
                                                       "TCAPOUT",
                                                       "HR1", "HE1", "HE2",
                                                       ])

    # remove unwanted columns for classification
#     del NCES_schools["LEAID"]
#     del NCES_schools["SURVYEAR"]

    # merge all three datasets                                           
    data = pd.concat([schools, NCES_schools, NCES_districts], axis=1)
#     length = len(data)
#     data = data.dropna()
#     print "\n[NaNs: dropped {} rows]".format(length - len(data))
# 
#     self.data = data
    pdb.set_trace() 
    censusdf = pd.read_csv("../data/district/SDDS_School_Districts_California_Jul-17-2014.csv")

if __name__ == "__main__":
    combine_data()
