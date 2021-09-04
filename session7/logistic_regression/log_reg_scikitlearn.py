
import numpy as np 

import matplotlib.pyplot as plt


from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


from sklearn import linear_model

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
 

#http://archive.ics.uci.edu/ml/machine-learning-databases/housing/

#http://archive.ics.uci.edu/ml/datasets/iris
#https://en.wikipedia.org/wiki/Iris_flower_data_set 
# https://towardsdatascience.com/lets-code-a-neural-network-in-plain-numpy-ae7e74410795



def get_data_diabetes():
 
 

    # Load the diabetes dataset
    diabetes = datasets.load_diabetes() 

    data_input = diabetes.data[:, np.newaxis, 2] 

    x_train = data_input[:-20]
    x_test = data_input[-20:]

    # Split the targets into training/testing sets
    y_train = diabetes.target[:-20]
    y_test = diabetes.target[-20:]

    # Split the data into training/testing sets

    return x_train, x_test, y_train, y_test



def get_data_iris():
  
    iris = datasets.load_iris() # https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

    data_input = iris.data[:, np.newaxis, 2] 

    x_train = data_input[:-60]
    x_test = data_input[-60:]

    # Split the targets into training/testing sets
    y_train = iris.target[:-60]
    y_test = iris.target[-60:]

    # Split the data into training/testing sets

    return x_train, x_test, y_train, y_test

def linear_reg_scipy(x_train, x_test, y_train, y_test):

    regr = linear_model.LinearRegression()
    regr.fit(x_train,  y_train) 
    print(regr.coef_) 
    error = np.mean((regr.predict(x_test) - y_test)**2) 
    print(error, 'is error') 
    r_score = regr.score(x_test, y_test)  # Explained variance score: 1 is perfect prediction
                                                  # and 0 means that there is no linear relationshipbetween X and y.

    print(r_score, 'is R score')



def logistic_reg_scipy(x_train, x_test, y_train, y_test):

     
    logistic = linear_model.LogisticRegression(solver='lbfgs', C=1e5, multi_class='multinomial')
    logistic.fit(x_train, y_train)  

    print(logistic.coef_) 
    error = np.mean((logistic.predict(x_test) - y_test)**2) 
    print(error, 'is error') 
    r_score = logistic.score(x_test, y_test)  # Explained variance score: 1 is perfect prediction
                                                  # and 0 means that there is no linear relationshipbetween X and y.

    print(r_score, 'is R score') # https://www.dummies.com/education/math/statistics/how-to-interpret-a-correlation-coefficient-r/

 

 


def main(): 



    x_train, x_test, y_train, y_test = get_data_diabetes()

    #https://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html

    print( ' run linear regression')

    linear_reg_scipy(x_train, x_test, y_train, y_test)


    print( ' run logistic regression')

    x_train, x_test, y_train, y_test = get_data_iris()
 
    logistic_reg_scipy(x_train, x_test, y_train, y_test)

     






if __name__ == '__main__':
    main()

