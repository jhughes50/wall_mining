"""
Testing Program: Calls correct functions depending how many classes are being tested
Jason Hughes
July 2020
"""


from wall_mining_utils import *
from feature_generator import featureGenerator

def test(number_of_classes):

	if number_of_classes == 2:

		Y, X = Main_2('lr')

	elif number_of_classes == 3:
	
		Y, X = Main_3()

	elif number_of_classes == 4:

		Y, X = Main_4()

	else:
		raise ClassError ('Program only supports testing with 2 or 3 classes')

	return Y, X

def Main_2(test):

	if test == 'wnw':

		df0, df1 = load_data(32)
	
	else:
	
		df0, df1 = load_left_right_data(24,5)

	df0 = trim_data(df0)
	df1 = trim_data(df1)
	print(len(df0))
	print(len(df1))

	fg = featureGenerator('gyro')

	df0_data = fg.transform(df0)
	df1_data = fg.transform(df1)

	final_data_0 = df0.join(df0_data)
	final_data_1 = df1.join(df1_data)

	data = final_data_0.append(final_data_1, sort = False)

	Y, X = get_train_test(data, len(df0), len(df1))

	return Y, X


def Main_3():

	df0, df1, df2 = Load_3_Data(24,5)

	df0 = trim_data(df0)
	df1 = trim_data(df1)
	df2 = trim_data(df2)
	print(len(df0))
	print(len(df1))
	print(len(df2))	
	
	fg = featureGenerator('gyro')

	df0_tdata = fg.transform(df0)
	df1_tdata = fg.transform(df1)
	df2_tdata = fg.transform(df2)

	final_data_0 = df0.join(df0_tdata)
	final_data_1 = df1.join(df1_tdata)
	final_data_2 = df2.join(df2_tdata)

	data = final_data_0.append(final_data_1, sort = False)
	data = data.append(final_data_2, sort = False)

	Y, X = get_train_test_3(data, len(df0), len(df1), len(df2))

	return Y, X

def Main_4():

	df0, df1, df2, df3 = Load_4_Data(24,5)
	print(len(df0))
	print(len(df1))
	print(len(df2))	
	print(len(df3))

	df0 = trim_data(df0)
	df1 = trim_data(df1)
	df2 = trim_data(df2)
	df3 = trim_data(df3)

	fg = featureGenerator('gyro')

	df0_tdata = fg.transform(df0)
	df1_tdata = fg.transform(df1)
	df2_tdata = fg.transform(df2)
	df3_tdata = fg.transform(df3)

	final_data_0 = df0.join(df0_tdata)
	final_data_1 = df1.join(df1_tdata)
	final_data_2 = df2.join(df2_tdata)
	final_data_3 = df3.join(df3_tdata)

	data = final_data_0.append(final_data_1, sort = False)
	data = data.append(final_data_2, sort = False)
	data = data.append(final_data_3, sort = False)

	Y, X = get_train_test_4(data, len(df0), len(df1), len(df2), len(df3))

	return Y, X
	







