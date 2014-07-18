#!/usr/bin/env python2.7 -B
""" find most important feautures when classifying DonorsChoose activity """

import pandas as pd
import numpy as np
import pdb

import merge # user-defined

# validation
from sklearn.cross_validation import train_test_split

# feature importance
from sklearn.ensemble import ExtraTreesClassifier


class Activity(object):
    """ DonorsChoose project activity """

    def __init__(self):
        pass


    def fetch_data(self):
        """ fetch DonorsChoose project data and NCES school and district finance data """
        print "[fetching data...]"

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

        # only look at data from 2011
        df2011 = df[df.year_posted == 2011].copy()

        # free from memory 
        del df

        # sort df by schools, custom aggregate on projects
        schools = df2011.groupby("_NCESid").agg({'_projectid': pd.Series.nunique,
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
#                                                        "FRELCH", "REDLCH",
                                                       "TOTFRL", 
                                                       "FTE",
#                                                        "ULOCAL", 
#                                                        "STATUS", "TYPE",
#                                                        "RECONSTY", "RECONSTF", 
#                                                        "CHARTR", "MAGNET",
#                                                        "MAGNET",
#                                                        "TITLEI", "STITLI", 
                                                       "MEMBER", "TOTETH", 
                                                       "WHITE", "BLACK",
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
        del NCES_schools["LEAID"]
        del NCES_schools["SURVYEAR"]

        # merge all three datasets                                           
        data = pd.concat([schools, NCES_schools, NCES_districts], axis=1)
        length = len(data)
        data = data.dropna()
        print "\n[NaNs: dropped {} rows]".format(length - len(data))

        self.data = data


    def define_label(self, n_projects=3):
        self.label = self.data.projects >= n_projects 
        del self.data["projects"]


    def correlation(self):
        """ compare project amount to many other factors using the pearson coefficient """
        print "\n[pearson coeffs...]"

        columns = ["percent_funded", "total_donations", "students_reached",
                   "TOTFRL", "STratio", "ETHpercent",
#                    "FRELCH", "REDLCH", 
                   "FTE", "TOTETH", 
                   "WHITE", "BLACK", "TOTALREV", "TSTREV", "TLOCREV", 
                   "TCAPOUT", "TOTALEXP"]
        temp = self.data[["projects", "MEMBER"] + columns].dropna()

        pearson_list = []
        for column in columns:
            pearson_list.append(  ( np.corrcoef(temp.projects, temp[column]/temp.MEMBER)[0,1], column )  )

        for p, name in sorted(pearson_list, key=lambda (p, name): p):
            print "[{:5.2f}] {}".format(p, name)


    def importance(self):
        """ compute feature importance using decision trees classifier """
        print "\n[decision tree classifier...]"

        clf = ExtraTreesClassifier()
        y = self.label.values
        X = self.data.values
        clf.fit(X, y)
        for imp, col in sorted(zip(clf.feature_importances_, self.data.columns), key = lambda (imp, col): imp, reverse = True):
            print "[{:.5f}] {}".format(imp, col)


if __name__ == "__main__":
    project_activity = Activity()
    project_activity.fetch_data()

    project_activity.correlation()

    project_activity.define_label()
    project_activity.importance()

