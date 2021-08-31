import numpy as np
import sympy as sym

x = sym.Symbol('x')
y = x**2 + sym.sin(sym.pi*x)

integral = sym.integrate(y, (x, -2, 2))

def riemann(h):
    sum = 0
    for i in range(int(4/h)):
        sum += h*y.subs(x, -2+i*h + h/2).evalf()
    return sum

def optimise(tol):
    error = 1
    h = 1
    while error > tol:
        h = h/2
        error = abs(integral-riemann(h))
    return h

def trap(h):
    sum = 0.5*h*y.subs(x, -2).evalf()
    for i in range(1, int(4/h)):
        sum += h*y.subs(x, -2+i*h).evalf()
    sum += 0.5*h*y.subs(x, 2).evalf()
    return sum

print(trap(0.25))