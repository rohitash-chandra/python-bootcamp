 
import numpy as np 
import random
import sys  # for end or endline in nested food loops, python 3
   

def sum_matrix(mat, cond):

    sum = 0
    conditional_sum = 0 
  
    for i in range(mat.shape[0]):          
        for j in range(mat.shape[1]):         
            print(mat[i,j], end=' ')
                   
        print()

    
    for i in range(mat.shape[0]):          
        for j in range(mat.shape[1]): 
            #print(sum, ' is accu sum')        
            sum = sum + mat[i,j] 
    
    for i in range(mat.shape[0]):          
        for j in range(mat.shape[1]): 
            if mat[i,j] > cond:   
                conditional_sum = conditional_sum + mat[i,j] 
                


                

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
