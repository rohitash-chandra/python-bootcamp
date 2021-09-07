#source: https://github.com/sydney-machine-learning/parallel-tempering-neural-net/blob/master/multicore-pt-regression/Compare_benchmark/nn.py

import sklearn
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor


def rmse(pred, actual): 
	return np.sqrt(((pred-actual)**2).mean())

def main():

	for i in range(1, 4) : 

		problem = i
		if problem ==	1:
			traindata = np.loadtxt("Data/Lazer/train.txt")
			testdata	= np.loadtxt("Data/Lazer/test.txt")	#
			name	= "Lazer"
		if problem ==	2:
			traindata = np.loadtxt(  "Data/Sunspot/train.txt")
			testdata	= np.loadtxt( "Data/Sunspot/test.txt")	#
			name	= "Sunspot"
		if problem ==	3:
			traindata = np.loadtxt("Data/Mackey/train.txt")
			testdata	= np.loadtxt("Data/Mackey/test.txt")  #
			name	= "Mackey" 
	
		x_train = traindata[:,0:3]
		y_train = traindata[:,4]
		x_test = testdata[:,0:3]
		y_test = testdata[:,4]
		
		mlp_adam = MLPRegressor(hidden_layer_sizes=(5, ), activation='relu', solver='adam', alpha=0.1,max_iter=5000, tol=0)
		mlp_adam.fit(x_train,y_train)
		y_predicttrain = mlp_adam.predict(x_train)
		y_predicttest = mlp_adam.predict(x_test)
		train_acc = rmse( y_predicttrain, y_train) 
		test_acc = rmse( y_predicttest, y_test) 

		print(name,train_acc, test_acc)
		
		mlp_sgd = MLPRegressor(hidden_layer_sizes=(5, ), activation='relu', solver='sgd', alpha=0.1,max_iter=5000, tol=0)
		mlp_sgd.fit(x_train,y_train)
		y_predicttrain = mlp_sgd.predict(x_train)
		y_predicttest = mlp_sgd.predict(x_test)
		train_acc = rmse( y_predicttrain,y_train) 
		test_acc = rmse( y_predicttest, y_test) 
		print(name,train_acc, test_acc)
		
		rf = RandomForestRegressor()
		rf.fit(x_train,y_train)
		y_predicttrain = rf.predict(x_train)
		y_predicttest = rf.predict(x_test)
		train_acc = rmse( y_predicttrain,y_train) 
		test_acc = rmse( y_predicttest, y_test)
		print(name,train_acc, test_acc)

if __name__ == "__main__": main()
