 
import numpy as np 
import random
import sys  # for end or endline in nested food loops, python 3


#1. implement function so that the sum is in between two values
#2 extend this function so it can apply to 3d matrix and 1d list
   

def sum_matrix(mat, cond):

    sum = 0
    conditional_sum = 0 

    dimen = 2


    if dimen == 1:
        for i in range(mat.shape[0]):   
            sum = sum + mat[i]   


    elif dimen == 2:
  
        '''for i in range(mat.shape[0]):          
            for j in range(mat.shape[1]):         
                print(mat[i,j], end=' ')    
            print()'''
        
        for i in range(mat.shape[0]):          
            for j in range(mat.shape[1]): 
                #print(sum, ' is accu sum')        
                sum = sum + mat[i,j] 
        
        for i in range(mat.shape[0]):          
            for j in range(mat.shape[1]): 
                if mat[i,j] > cond:   
                    conditional_sum = conditional_sum + mat[i,j] 

    else: # dimen is 3
        print(' x')
                


                

    return sum, conditional_sum




def main(): 

    print('running: sum of matrix ()')
    
    length = 3
    width = 4
    height = 5

    
    mat = np.random.rand(length, width)

    #mat_threedimen = np.zeros((length, width, height))
    mat_threedimen = np.random.rand(length, width, height)
    
    print(mat_threedimen)
    print(mat)


    cond = 0.2


    sum_mat, cond_sum = sum_matrix(mat, cond)


    print(sum_mat, cond_sum, ' sum and cond sum')


 
 
if __name__ == '__main__':
    main()
