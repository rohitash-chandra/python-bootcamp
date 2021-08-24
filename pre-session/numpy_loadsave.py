#!/usr/bin/env python

'''
A Python program  

'''
import numpy as np 

import matplotlib.pyplot as plt


import random


import sys  # for end or endline in nested food loops, python 3
 

def plot_examples():
  x = [1, 2, 3, 4]
  #numpy_x = 
  plt.plot(x)
  plt.ylabel('some numbers')
  #plt.show()
  plt.savefig('x.png')

  plt.clf() # make sure you have this in all plots
 

  
 

def numpy_design(filename):

  #a = np.zeros((10,10))

  b = np.random.rand(10,10)
 
  for x in range(1, b.shape[0]):
    for y in range(1, b.shape[1], 2):
        b[x][y] = y*x 

  double_mat =   b * 2

 #https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
  np.savetxt(filename, double_mat, delimiter = ' ',  fmt='%1.2f' )
  np.savetxt('mymagic.csv', double_mat, delimiter = ',',  fmt='%1.2f' )
  np.savetxt('mymagic_fmt.csv', double_mat, delimiter = ',',  fmt='%1.5f' )
 



def load_file(filename):

 #https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
  data_load = np.loadtxt(filename)

  print(data_load, ' loaded data')

  plt.imshow(data_load, cmap='hot', interpolation='nearest')
  plt.savefig('design_magic.png')
  plt.clf() # make sure you have this in all plots

  #https://matplotlib.org/gallery/images_contours_and_fields/image_annotated_heatmap.html

  data_tras = np.transpose(data_load)


  plt.imshow(data_tras, cmap='hot', interpolation='nearest')
  plt.savefig('design_magic_traspose.png')
  plt.clf() # make sure you have this in all plots
 
   

 








 


def main(): 
 
 

    filename = 'mymagic.txt' # filename to  output data and also read data later

    numpy_design(filename)

    plot_examples()

    load_file(filename)
 
 



if __name__ == '__main__':
    main()
