 
import numpy as np 
import random
import sys  # for end or endline in nested food loops, python 3
   

def nested_loops():

  print(' nested loops function')
  #https://www.ict.social/python/basics/multidimensional-lists-in-python

  length = 3
  width = 4
  height = 5

  two_dimen = np.random.rand(length, width)
  print(two_dimen)

  first_row = two_dimen[0,:]
  second_col =   two_dimen[:,1]

  print(first_row, ' first_row') 
  print(second_col, ' second_col') 

  three_dimen = np.zeros((length, width, height))

  print(three_dimen)

  for i in range(length):         #0
    for j in range(width):        #0 1 2 3
      two_dimen[i,j] = i*j        #1
                                  #0 1 2 3
  print (two_dimen)  

      #print (k, end =' ')  # end refers new line
  print (' 3 nested ')
  for i in range(1,3):                  
    for j in range(1,3):
      for k in range(1,3):
        z = i*j * k
        print (z)  # end refers new line 


  print (' 3 nested save to np array ')

  for i in range(length):
    for j in range(width):
      for k in range(height):
        three_dimen[i,j,k] = i*j * k
  print(three_dimen, ' ** ')

  last_two_rows = three_dimen[2,2:4,3:5]

  print(last_two_rows, ' **** ')
  #operations to select parts of 2d array
         

# i is your mat
# j is your row
# k is your col

# 0 is mat
# 0 is row
# 0 1 2 3 is col

# 0 is mat
# 1 is row
# 0 1 2 3 is col


# 0 is mat
# 2 is row
# 0 1 2 3 is col


# 0 is mat
# 3 is row
# 0 1 2 3 is col


# 1 is mat
# 0 is row
# 0 1 2 3 is col

# 1 is mat
# 1 is row
# 0 1 2 3 is col





 
def main(): 



    print('running: nested_loops()')
    nested_loops()
 
if __name__ == '__main__':
    main()
