"""
Main Program for wall data mining research project
Jason Hughes
July 2020
"""

import pandas as pd
import numpy as np
import time

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from wall_mining_utils import *
from wall_mining_testing import *
from feature_generator import featureGenerator

number_of_classes = 4

Y, X = test(number_of_classes)

acc_list = []

for i in range(10):

	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle = True)

	clf = BaggingClassifier()
	y_test = y_test.values.tolist()
	clf.fit(X_train, y_train)
	X_predict = clf.predict(X_test)

	accuracy = score(X_predict, y_test)
	acc_list.append(accuracy)
	print(accuracy)

print('LR BAG')
print('AVG: ',sum(acc_list)/len(acc_list))
