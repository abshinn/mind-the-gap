#!/usr/bin/env python2.7
"""find most important feautures when classifying DonorsChoose activity"""

import pandas as pd
import numpy as np
# import pdb

# validation
from sklearn.cross_validation import train_test_split

# feature importance
from sklearn.ensemble import ExtraTreesClassifier


class dcActivity(object):

    def __init__(self):
        pass

    def fetch_data(self):
        pass

    def train(self):
        pass

    def importance(self):
        clf = ExtraTreesClassifier()
        y = self.label.values
        X = self.data.values
        clf.fit(X, y)
        for imp, col in sorted(zip(clf.feature_importances_, self.data.columns), key = lambda (imp, col): imp, reverse = True):
            print "[{:.5f}] {}".format(imp, col)


if __name__ == "__main__":
    pass
