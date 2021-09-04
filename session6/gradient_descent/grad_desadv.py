#~ source: https://en.wikipedia.org/wiki/Gradient_descent
#https://en.wikipedia.org/w/index.php?title=Gradient_descent&oldid=966271567
# set up a stepsize multiplier
gamma = 0.003

# set up a number of iterations
iter = 500

# define the objective function f(x) = x^4 - 3*x^3 + 2
objFun = function(x) return(x^4 - 3*x^3 + 2)

# define the gradient of f(x) = x^4 - 3*x^3 + 2
gradient = function(x) return((4*x^3) - (9*x^2))

# randomly initialize a value to x
set.seed(100)
x = floor(runif(1, 0, 10))

# create a vector to contain all xs for all steps
x.All = numeric(iter)

# gradient descent method to find the minimum
for(i in seq_len(iter)){
        x = x - gamma*gradient(x)
        x.All[i] = x
        print(x)
}

# print result and plot all xs for every iteration
print(paste("The minimum of f(x) is ", objFun(x), " at position x = ", x, sep = ""))
plot(x.All, type = "l")
