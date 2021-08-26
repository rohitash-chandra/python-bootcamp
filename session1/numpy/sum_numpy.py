import numpy as np 
 
import random 

def numpy_lists():
 
 magic = np.random.rand(3,4)
 magic_three = np.random.rand(3,4,2)
 # homework, write a function for summing 3D magic
 magic_one = np.random.rand(10)

 #print(magic)
 #print(magic_one)
 print(magic_three)
 print(magic.shape)

 magic_sum = sum_numpy(magic)
 print( magic_sum, ' is magic sum')
 return magic_sum

def sum_numpy(a):
  sum = 0
  for x in range(a.shape[0]):
    for y in range(a.shape[1]):
        print(x, y, ' *' , a[x][y] )
        sum = sum + a[x][y]
  return sum 

def sum_3D(a):
  print('homework - sum elements of 3d numpy array')

  # use nested for loops
  #https://www.ict.social/python/basics/multidimensional-lists-in-python


def main(): 

    print('running: numpy_lists()')
    sum = numpy_lists()
    print(sum, ' is sum')
 
 


if __name__ == '__main__':
    main()

