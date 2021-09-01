


# Rohitash Chandra, 2021 c.rohitash@gmail.conm

#https://github.com/rohitash-chandra
  
 

import matplotlib.pyplot as plt
import numpy as np 
import random
import time


from numpy import *


from sklearn.preprocessing import Normalizer

from sklearn.model_selection import train_test_split 


#Source: https://github.com/sydney-machine-learning/multilayerperceptron-sgd-adam/blob/main/fnn-multiplelayers.py




class Layers:

	def __init__(self, first, second,adam_learnrate=None):  
		#self.number = first

		self.weights = np.random.uniform(-0.5, 0.5, (first , second))   
		self.bias = np.random.uniform(-0.5,0.5, (1, second))  # bias second layer

		self.output = np.zeros(second) # output of  layer 
		self.gradient = np.zeros(second) # gradient of layer 
 

class Network:

	def __init__(self, topology, x_train, x_test, y_train, y_test, max_epocs,   min_error, learn_rate): # this is called construtor
		self.topology  = topology   

		self.output_activationfunc = 'sigmoid' 

		self.max_epocs = max_epocs # max epocs
		#self.TrainData = Train
		#self.TestData = Test

		self.x_train = x_train
		self.x_test = x_test
		self.y_train = y_train
		self.y_test = y_test


		self.num_samples =  x_train.shape[0] 

		self.sgdlearn_rate  = learn_rate
 

		self.min_error = min_error 
		 
		np.random.seed()   

		self.adam_learnrate = 0.05 #sensitive for adam
 

		self.end_index = len(self.topology)-1


		self.layer = [None]*20  # create list of Layers objects ( just max size of 20 for now - assuming a very deep neural network )

		print(self.topology,  ' topology')

		self.layer[0] = Layers(1,1, 0) # this is just for layer where input features are stored

		for n in range(1,  len(self.topology)):  
			self.layer[n] = Layers(self.topology[n-1],self.topology[n], self.adam_learnrate)


	def print_network(self):

		for n in range(1, self.end_index+1):  
			#note layer 0 weights and biases are not needed. 
			print(n, ' is layer')
			print(n, self.layer[n].output)
			print(n, self.layer[n].weights)
 

	def activation(self,x):
		if  self.output_activationfunc == 'sigmoid':
			return 1 / (1 + np.exp(-x)) 

		else:
			return x # linear acivation
	 
		return exps / np.sum(exps, axis=0)

	def individual_error(self,desired):
		error = np.subtract(self.layer[self.end_index].output, desired)
		sq_error= np.sum(np.square(error))/self.topology[self.end_index] 
		return sq_error

	def forward_pass(self, input_features ): 

		self.layer[0].output = input_features 

		for n in range(0, self.end_index):  
			z = self.layer[n].output.dot(self.layer[n+1].weights) - self.layer[n+1].bias 
			self.layer[n+1].output = self.activation(z) 


	def backpropagation(self, optimiser):  

		data_features = np.zeros((1, self.topology[0])) # temp hold input
		desired = np.zeros((1, self.topology[self.end_index])) 
 
		epoch = 0
		best_mse = 10000 # assign a large number in begining to maintain best (lowest RMSE)
		best_train = 0
		while  epoch < self.max_epocs and best_train < self.min_error :
			sse = 0
			for s in range(0, self.num_samples):

				data_features[:]  =  self.x_train[s,:]  
 
				desired[:]  = self.y_train[s,:] 
 
				self.forward_pass(data_features)

				print(self.layer[self.end_index].output, ' is predicted')
				print(desired, ' is desired')

				'''if optimiser == 'adam':
					self.backwardpass_advancedgradients(data_features ,desired)
				else: 
					self.backward_pass(data_features ,desired)'''


				sse = sse+ self.individual_error(desired)
			 
			mse = np.sqrt(sse/self.num_samples*self.topology[self.end_index])
 
 
			
			epoch=epoch+1  
 

		return (mse) 

# OOP (class) ends

# ---------------------------------------------------------------------------------------------


# -- normal functions from below (no self as parameter)

def read_data(problem):

	if problem ==1:
		#Source:  Pima-Indian diabetes dataset: https://www.kaggle.com/kumargh/pimaindiansdiabetescsv
		data_in = genfromtxt("data/pima-indians-diabetes.csv", delimiter=",")
		data_inputx = data_in[:,0:8] # all raw features 0, 1, 2, 3, 4, 5, 6, 7 
		transformer = Normalizer().fit(data_inputx)  # fit does nothing. (scikit learn)
		data_inputx = transformer.transform(data_inputx)

		data_inputy = data_in[:,-1] # this is target - so that last col is selected from data

		# needs one hot encoding 
	elif problem ==2:
		#Iris with one hot encoded labels
		data_in = genfromtxt("data/iris.csv", delimiter=",")
		data_inputx = data_in[:,0:4] # all raw features [0, 1, 2, 3]
		transformer = Normalizer().fit(data_inputx)  # fit does nothing. (scikit learn)
		data_inputx = transformer.transform(data_inputx)
 
		data_inputy = data_in[:,4:7] # one hot encded labels (3 classes) [4,5,6]


	elif problem ==3: 
		#wine
		data_in = genfromtxt("data/wine.csv", delimiter=",")
		data_inputx = data_in[:,0:13] # all features [0, 1, 2, 3, ... 12] (13 raw features )
		#data_inputx = transformer.transform(data_inputx)
		data_inputy = data_in[:,-1] # 
		

		# needs one hot encoding 

	else:
		print('else')


	x_train, x_test, y_train, y_test = train_test_split(data_inputx, data_inputy, test_size=0.90, random_state=1)

	return x_train, x_test, y_train, y_test

def main(): 

	#assume you use one hot encoding always in labels for classification problems
					
	problem = 2 # iris works, rest need one hot encoding fixed

	x_train, x_test, y_train, y_test  = read_data(problem)

	print(x_train, y_train, ' x_train,  y_train ')

	input_features = x_train.shape[1]
	num_outputs =  y_train.shape[1]

	learn_rate = 0.1  

	hidden = 5 # let user decide for prob
 
	#topo = [input_features,   hidden, hidden,  num_outputs] 


	topo = [input_features,    hidden,  num_outputs] 

	max_time = 1 # how many epochs needed for training the neural network

	min_criteria = 0.01 # minumum error on training data (to stop early )

	fnn = Network(topo, x_train, x_test, y_train, y_test, max_time,   min_criteria, learn_rate)

	fnn.print_network()

	mse = fnn.backpropagation('sgd')

	print(mse, '  mse')



if __name__ == "__main__": main()

