

# https://en.wikipedia.org/wiki/Factorial


import time


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        fact = x * factorial(x-1)
        #print(x, fact, ' is fact')
        return fact
        



def factorial_iteration(num):
    fac = 1
 
    for i in range(1, num + 1):
        fac = fac * i
        #print(i, fac, ' is fact by iteration')
    return fac



#----------------------------------------

num = 900



start = time.time() 
 
fact = factorial(num)

end = time.time()


print("The factorial using RECURSION of", num, "is", fact)

print('RECURSION took time: ', end - start)



start = time.time() 

fact_iteration = factorial_iteration(num)

end = time.time()


print("The factorial using ITERATION of", num, "is", fact_iteration)


print('ITERATION took time: ', end - start)


