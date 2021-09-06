import numpy as np 

import matplotlib.pyplot as plt


from numpy import *
 

import random

  





def read_data():
    #Source: University of California. (n.d). Machine-learning-databases. http://archive.ics.uci.edu/ml/machine-learning-databases/housing/
    #Source: University of California. (n.d). Machine learning repository. http://archive.ics.uci.edu/ml/datasets/iris 
    #Source: Iris flower dataset. (2020). Wikipedia. https://en.wikipedia.org/wiki/Iris_flower_data_set


    #data_in = genfromtxt("data/iris_onehotenc.csv", delimiter=",") # path will change -  in case of windows \ will be used 

    data_in = genfromtxt("data/iris_binaryenc.csv", delimiter=",")



    data_inputx = data_in[:,0:4] # all features 0, 1, 2, 3

    #data_inputx = data_in[:,[1]]  # one feature

    #data_inputx = data_in[:,[1,2]]  # two features

    data_inputy = data_in[:,-1] # this is target - so that last col is selected from data

    x_train = data_inputx[:-20]
    x_test = data_inputx[-20:]

    # Split the targets into training/testing sets
    y_train = data_inputy[:-20]
    y_test = data_inputy[-20:] 


    #percentage 
    
    #random data split

    return x_train, x_test, y_train, y_test
 
     


def main(): 
 
 
    x_train, x_test, y_train, y_test = read_data()  

    print(x_train, ' x_train')
    print(y_train, ' y_train')  

    mean_xtrain = np.mean(x_train, axis=0)

    print(mean_xtrain, ' mean_xtrain')


    std_xtrain = np.std(x_train, axis=0)

    print(std_xtrain, ' std_xtrain')

    cov = np.cov(x_train)

    
    print("Covarinace matrix of x:\n", cov)

    #todo - write functions to implement mean, std, and cov from sctach using for loops and arrays



if __name__ == '__main__':
     main()

