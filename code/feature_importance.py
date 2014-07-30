#!/usr/bin/env python2.7 -B
""" find most important feautures when classifying DonorsChoose activity """

import pandas as pd
import numpy as np

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report


def correlation(data, columns=[]):
    """Compare project amount to other features using the pearson coefficient.

    INPUT: data    -- pandas dataframe
           columns -- list of column names to compare to project amount
    """

    if not columns:
        columns = ["percent_funded", "total_donations", "students_reached",
                   "TOTFRL", "STratio", "ETHpercent", "FTE", "TOTETH", 
                   "WHITE", "BLACK", "TOTALREV", "TSTREV", "TLOCREV", 
                   "TCAPOUT", "TOTALEXP"]

    temp = data[["projects", "MEMBER"] + columns].dropna()

    pearson_list = []
    for column in columns:
        pearson_list.append(  ( np.corrcoef(temp.projects, temp[column]/temp.MEMBER)[0,1], column )  )

    for p_value, name in sorted(pearson_list, key=lambda (p_value, name): p_value):
        print "[{:5.2f}] {}".format(p_value, name)


def define_label(data, n_projects=3):
    """Define label with which to train classifier on.

    INPUT: data       -- pandas dataframe
           n_projects -- asign True for amount of projects greater than or equal to n_projects

    OUTPUT: tuple (data, label)
            data  -- pandas dataframe without project column or non-numeric columns
            label -- pandas boolean series 
    """

    label = data.projects >= n_projects 
    data = data.drop(["projects"], axis=1)._get_numeric_data()
    return data, label


def importance(data, label):
    """Compute feature importance using decision trees classifier.

    INPUT: data  -- numeric pandas dataframe with non-negative, non-missing values
           label -- boolean pandas series with which to predict on

    OUTPUT: results sent to stdout
    """

    clf = RandomForestClassifier()
    clf.fit(data.values, label.values)

    scores = cross_validation.cross_val_score(clf, data, label, cv=3, scoring="roc_auc")
    print "\ncv scores: {}\n".format(scores)

    for imp, col in sorted( zip(clf.feature_importances_, data.columns), key=lambda (imp, col): imp, reverse=True ):
        print "[{:.5f}] {}".format(imp, col)
