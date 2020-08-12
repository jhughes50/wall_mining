"""
Utility functions for wall data mining research project
Jason Hughes
July 2020
"""

import pandas as pd
import numpy as np


def load_data(number_of_files):


	attributes = ['acc.x','acc.y','acc.z','gyro.x','gyro.y','gyro.z','stateEstimate.x',\
'stateEstimate.y','stateEstimate.z','stabilizer.pitch','stabilizer.roll']

	wall_data = pd.DataFrame(data=[], columns = attributes)
	no_wall_data = pd.DataFrame(data=[], columns = attributes)

	for j in range(5):
		for i in range(24):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_left_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				wall_data = wall_data.append(temp, sort = False)
			except FileNotFoundError:
				pass
	for j in range(5):
		for i in range(24):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_right_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				wall_data = wall_data.append(temp, sort = False)
			except FileNotFoundError:
				pass
	
	class_wall = []

	for k in range(len(wall_data)):
		class_wall.append(1)

	wall_data['class'] = class_wall

	for j in range(6):

		try:
			filename = 'Original_csv/trans_data/class_nowall/data_wall_transition_nowall' + repr(j) + '.csv'
			temp = pd.read_csv(filename)
			temp = temp.drop(columns = ['Unnamed: 0','baro.pressure'])
			no_wall_data = no_wall_data.append(temp, sort = False)
		except FileNotFoundError:
			pass


	class_nowall = []
	
	for k in range(len(no_wall_data)):
		class_nowall.append(0)

	no_wall_data['class'] = class_nowall

	data = wall_data.append(no_wall_data, sort = False)

	return wall_data, no_wall_data

def load_left_right_data(number_of_files,tests):

	attributes = ['acc.x','acc.y','acc.z','gyro.x','gyro.y','gyro.z','stateEstimate.x',\
'stateEstimate.y','stateEstimate.z','stabilizer.pitch','stabilizer.roll']

	left = pd.DataFrame(data=[], columns = attributes)
	right = pd.DataFrame(data=[], columns = attributes)

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_left_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				left = left.append(temp, sort = False)
			except FileNotFoundError:
				pass

	

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_right_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				right = right.append(temp, sort = False)
			except FileNotFoundError:
				pass

	class_left = []
	class_right = []

	for k in range(len(left)):
		class_left.append(0)

	left['class'] = class_left

	for k in range(len(right)):
		class_right.append(1)

	right['class'] = class_right

	return left, right

def trim_data(data):

	data = data.drop(columns = ['acc.x','acc.y', 'acc.z', 'stateEstimate.x', 'stateEstimate.y','stateEstimate.z'])


	i = [x for x in range(len(data))]

	data.index = i

	return data


def get_train_test(data, last_0, last_1):

	i = [x for x in range(len(data))]
	data.index = i
	
	data = data.drop([last_0-1,last_1+last_0-1])

	test = data['class']
	train = data.drop(columns = ['class'])

	return test, train



def score(predict, actual):

	equal = 0

	for i in range(len(predict)):

		if predict[i] == actual[i]:
			equal += 1

	score = equal / len(predict)
	
	return score

def Load_3_Data(number_of_files, tests):

	attributes = ['acc.x','acc.y','acc.z','gyro.x','gyro.y','gyro.z','stateEstimate.x',\
'stateEstimate.y','stateEstimate.z','stabilizer.pitch','stabilizer.roll']

	left = pd.DataFrame(data=[], columns = attributes)
	right = pd.DataFrame(data=[], columns = attributes)
	front = pd.DataFrame(data=[], columns = attributes)

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_left_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				left = left.append(temp, sort = False)
			except FileNotFoundError:
				pass

	

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_right_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				right = right.append(temp, sort = False)
			except FileNotFoundError:
				pass

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_front_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				front = front.append(temp, sort = False)
			except FileNotFoundError:
				pass

	class_left = [0 for k in range(len(left))]
	class_right = [1 for k in range(len(right))]
	class_front = [2 for k in range(len(front))]

	left['class'] = class_left
	right['class'] = class_right
	front['class'] = class_front

	return left, right, front	


def get_train_test_3(data, last_0, last_1, last_2):

	i = [x for x in range(len(data))]
	data.index = i
	
	data = data.drop([last_0-1,last_1+last_0-1, last_0+last_1+last_2-1])
	data.to_csv('test.csv')
	test = data['class']
	train = data.drop(columns = ['class'])

	return test, train


def Load_4_Data(number_of_files, tests):

	attributes = ['acc.x','acc.y','acc.z','gyro.x','gyro.y','gyro.z','stateEstimate.x',\
'stateEstimate.y','stateEstimate.z','stabilizer.pitch','stabilizer.roll']

	left = pd.DataFrame(data=[], columns = attributes)
	right = pd.DataFrame(data=[], columns = attributes)
	front = pd.DataFrame(data=[], columns = attributes)
	no_wall_data = pd.DataFrame(data=[], columns = attributes)

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_left_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				left = left.append(temp, sort = False)
			except FileNotFoundError:
				pass

	

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_right_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				right = right.append(temp, sort = False)
			except FileNotFoundError:
				pass

	for j in range(tests):
		for i in range(number_of_files):

			try:
				filename = 'Original_csv/trans_data/class_1/transition_front_' + repr(j) +\
 '_second_' + repr(i) + '.csv'
				temp = pd.read_csv(filename)
				temp = temp.drop(columns = ['Unnamed: 0'])
				front = front.append(temp, sort = False)
			except FileNotFoundError:
				pass

	for j in range(3):

		try:
			filename = 'Original_csv/trans_data/class_nowall/data_wall_transition_nowall' + repr(j) + '.csv'
			temp = pd.read_csv(filename)
			temp = temp.drop(columns = ['Unnamed: 0','baro.pressure'])
			no_wall_data = no_wall_data.append(temp, sort = False)
		except FileNotFoundError:
			pass


	class_left = [0 for k in range(len(left))]
	class_right = [1 for k in range(len(right))]
	class_front = [2 for k in range(len(front))]
	class_nowall = [3 for k in range(len(no_wall_data))]

	left['class'] = class_left
	right['class'] = class_right
	front['class'] = class_front
	no_wall_data['class'] = class_nowall

	return left, right, front, no_wall_data


def get_train_test_4(data, last_0, last_1, last_2, last_3):

	i = [x for x in range(len(data))]
	data.index = i
	
	data = data.drop([last_0-1,last_1+last_0-1, last_0+last_1+last_2-1, last_0+last_1+last_2+last_3-1])
	#data.to_csv('test.csv')
	test = data['class']
	train = data.drop(columns = ['class'])

	return test, train



