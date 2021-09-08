#~ source: https://en.wikipedia.org/wiki/Gradient_descent 
# set up a stepsize multiplier
gamma = 0.003

# set up a number of iterations
iter = 500

# define the objective function f(x) = x^4 - 3*x^3 + 2
def function(x): 
    return(x^4 - 3*x^3 + 2)

# define the gradient of f(x) = x^4 - 3*x^3 + 2
def gradient(x):
    return((4*x^3) - (9*x^2))
 
 

# complete this code by using gradient descent alg
