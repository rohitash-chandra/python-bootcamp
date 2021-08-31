import math


# Source: https://computation.physics.utoronto.ca/python-reference/learning-examples/numerical-integration/


#the function to be integrated:
def func(x):
    return x ** 4 * (1 - x) ** 4 / (1 + x ** 2)
 
#define a function to do integration of f(x) btw. 0 and 1:

def trap(func, n):
    h = 1 / float(n)
    intgr = 0.5 * h * (func(0) + func(1))
    for i in range(1, int(n)):
        intgr = intgr + h * func(i * h)
    return intgr
 
print(trap(func, 100))



