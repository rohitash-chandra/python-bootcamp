


'''
A Python program  

'''
import numpy as np 

import matplotlib.pyplot as plt


import random





def advanced_numpy():

  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html

  a = np.array([1, 2, 3])
  b = np.array([2, 3, 4])

  vertical_stack = np.vstack((a,b))
  print(vertical_stack, '  vertical_stack')

  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.hstack.html#numpy.hstack

  horizontal_stack = np.hstack((a,b))
  print(horizontal_stack, '  horizontal_stack')

  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html#numpy.concatenate

  a = np.array([[1, 2], [3, 4]])
  b = np.array([[5, 6]])
  ab = np.concatenate((a, b), axis=0)
  print(ab, '  concatenate  axis=0')

  ab = np.concatenate((a, b.T), axis=1)  # note b.T is same is b.transpose()
  print(ab, '  concatenate  axis=1')

  ab = np.concatenate((a, b), axis=None)
  print(ab, '  concatenate  axis= none')

  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.split.html#numpy.split

  x = np.arange(9.0)
  x_split = np.split(x, 3)

  print(x, '  original x')

  print(x_split, '  x split into three')

  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html

  z = np.arange(6) # produces and array of 0 - 5
  print(z, '  original z')

  z_reshape = z.reshape((3, 2))
  print(z_reshape, '  reshaped z')

  z_flat = np.reshape(z_reshape, 6)
  print(z_flat, '  flatten z')

  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html

  z_flat= z_reshape.flatten()
  print(z_flat, '  another way to flatten z')
 
 




def main(): 
 

    advanced_numpy() 



if __name__ == '__main__':
    main()
