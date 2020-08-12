import numpy as np
import pandas as pd
import math


class featureGenerator:

	def __init__(self, attribute, sliding_window = 1):

		self.attribute = attribute
		self.sliding_window = sliding_window


	def calc_angles(self, roll, pitch):

		angles = []
		
		start = 0
		end = 100
		
		for i in range(len(roll)):
		
			sw_r = roll.iloc[start:end]
			sw_p = pitch.iloc[start:end]

			theta = sw_r.mean()
			phi = sw_p.mean()
		

			theta = (theta * math.pi) / 180
			phi = (phi * math.pi) / 180

			Pu = [np.sin(phi), 0, np.cos(phi)]
			Ru = [0, np.sin(theta), np.cos(theta)]

			Z = []

			for q in range(len(Pu)):
				Z.append(Pu[q] + Ru[q])

			Z[2] = 0

			i = Z[0]
			j = Z[1]

			angles.append(np.arctan(i/j))

			start = start + self.sliding_window
			end = end + self.sliding_window

		return angles


	def calc_cos_angles(self, roll, pitch):

		angles = []
		
		start = 0
		end = 100

		for i in range(len(roll)):
			
			sw_r = roll.iloc[start:end]
			sw_p = pitch.iloc[start:end]
			
			roll_a = sw_r.mean()
			pitch_a = sw_p.mean()

			cr = math.cos(roll_a * math.pi / 180)
			cp = math.cos(pitch_a * math.pi / 180)
		
			angles.append( (180/math.pi) * math.atan2(cp,cr) )

			start = start + self.sliding_window
			end = end + self.sliding_window

		return angles


	def get_new_columns(self):

		features = ['mu', 'sigma', 'mad']
		columns = []

		for f in features:
		
			columns.append(f + '.x')
			columns.append(f + '.y')
			columns.append(f + '.z')
			columns.append(f + '.r')
			columns.append(f + '.p')

		return columns


	def calculate_avg_resultant(self,x,y,z):

		avg_res = []
		x = x.values.tolist()
		y = y.values.tolist()
		z = z.values.tolist()

		for i in range(len(x)):

			a = abs(x[i]) ** 0.5
			b = abs(y[i]) ** 0.5
			c = abs(z[i]) ** 0.5

			avg_res.append((a+b+c)/3)

		return avg_res
	
	
	def calculate_mean_std(self,x,y,z,r,p):

		start = 0
		end = start + 100

		mu_x = []
		mu_y = []
		mu_z = []
		mu_r = []
		mu_p = []

		sigma_x = []
		sigma_y = []
		sigma_z = []
		sigma_r = []
		sigma_p = []

		mad_x = []
		mad_y = []
		mad_z = []
		mad_r = []
		mad_p = []

		for i in range(len(x)):

			sw_x = x.iloc[start:end]
			mu_x.append(sw_x.mean())
			sigma_x.append(sw_x.std())	
			mad_x.append(sw_x.mad())

			sw_y = y.iloc[start:end]
			mu_y.append(sw_y.mean())
			sigma_y.append(sw_y.std())
			mad_y.append(sw_y.mad())

			sw_z = z.iloc[start:end]
			mu_z.append(sw_z.mean())
			sigma_z.append(sw_z.std())
			mad_z.append(sw_z.mad())

			sw_r = r.iloc[start:end]
			mu_r.append(sw_r.mean())
			sigma_r.append(sw_r.std())
			mad_r.append(sw_r.mad())

			sw_p = p.iloc[start:end]
			mu_p.append(sw_p.mean())
			sigma_p.append(sw_p.std())
			mad_p.append(sw_p.mad())

			start = start +  self.sliding_window
			end = end + self.sliding_window
		
		new_cols = self.get_new_columns()

		n_arr = np.stack((mu_x, mu_y, mu_z, mu_r, mu_p, sigma_x, sigma_y, sigma_z, sigma_r, sigma_p, mad_x, mad_y, mad_z, mad_r, mad_p))
		new_feat_df = pd.DataFrame(n_arr.T, columns = new_cols)

		return new_feat_df

	def compose_final_df(self, new_df, avg_res, angles, cos_angles):

		new_df['average.resultant'] = avg_res
		new_df['angle'] = angles
		new_df['cos.angles'] = cos_angles		
	
		return new_df

	def transform(self, data):

		x = data['gyro.x']
		y = data['gyro.y']
		z = data['gyro.z']
		r = data['stabilizer.roll']
		p = data['stabilizer.pitch']

		new_df = self.calculate_mean_std(x,y,z,r,z)

		avg_res = self.calculate_avg_resultant(x,y,z)

		angles = self.calc_angles(r,p)
		
		cos_angles = self.calc_cos_angles(r,p)

		final_df = self.compose_final_df(new_df, avg_res, angles, cos_angles)

		return final_df

	
