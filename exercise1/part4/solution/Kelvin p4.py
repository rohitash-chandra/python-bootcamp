import numpy as np
import sympy as sym

x = sym.Symbol('x')
y = x**2 + sym.sin(sym.pi*x)                        #Looks like x^2 + sin(pi*x)

integral = sym.integrate(y, (x, -2, 2))             #Real integral value. (was just integral of x^2 since sin odd)

def riemann(h):
    sum = 0
    for i in range(int(4/h)):                       #Guess I couldve used 4//h 
        sum += h*y.subs(x, -2+i*h + h/2).evalf()
    return sum

def optimise(tol):
    error = 1                                       #initialise error that would start the while loop
    h = 1
    while error > tol:
        h = h/2                                     #Checks optimal size as 1/2^n
        error = abs(integral-riemann(h))            #Gets updated anyway
    return h

def trap(h):
    sum = 0.5*h*y.subs(x, -2).evalf()
    for i in range(1, int(4/h)):
        sum += h*y.subs(x, -2+i*h).evalf()
    sum += 0.5*h*y.subs(x, 2).evalf()
    return sum
