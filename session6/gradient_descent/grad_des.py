#~source: https: //en.wikipedia.org/wiki/Gradient_descent
# code source: https://en.wikipedia.org/w/index.php?title=Gradient_descent&oldid=966271567

next_x = 6# We start the search at x = 6
gamma = 0.01# Step size multiplier
precision = 0.00001# Desired precision of result
max_iters = 10000# Maximum number of iterations

# Derivative
#function
def df(x):
  return 4 * x ** 3 - 9 * x ** 2

for i in range(max_iters):
    current_x = next_x
    next_x = current_x - gamma * df(current_x)
    print(i, next_x, df(current_x))

    step = next_x - current_x
    if abs(step) <= precision:
        break

print("Minimum at ", next_x)

# The output for the above will be something like 
# "Minimum at 2.2499646074278457"
