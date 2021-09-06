# simulated annealing search of a one-dimensional objective function

#Source https://machinelearningmastery.com/simulated-annealing-from-scratch-in-python/


from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

# objective function
def objective(x):
	return x[0]**2.0   # y = x*x      y= y^2 

def objective_func(x): # vectorized version (more than 1 dimen)
	sum = 0

	for i in range(len(x)):
		sum+= x[i]**2.0 
	return  sum # y = x*x      y= y^2 

'''for i in range(-5,5):
	x= randn()
	print(x, objective([x]), ' is the y - ') 

print(objective_func([3, 4.9, 1, 2, -5]), ' is the y ') '''

#-0.6015083563080654 0.3618123027084306  is the y
# make a neighbour

'''x = -0.6015083563080654
print(x, objective([x]), ' is the y *') 


x = -0.6115083563080654
print(x, objective([x]), ' is the y **') '''


#[3.5]
#[3.5, 3.1, 4.1]

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
	# generate an initial point
	best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# evaluate the initial point
	best_eval = objective(best)
	# current working solution
	curr, curr_eval = best, best_eval
	# run the algorithm

	count_better = 0

	count_weaker = 0

	for i in range(n_iterations):
		# take a step
		candidate = curr + randn(len(bounds)) * step_size
		# evaluate candidate point
		candidate_eval = objective(candidate)
		# check for new best solution
		if candidate_eval < best_eval:
			# store new best point
			best, best_eval = candidate, candidate_eval
			# report progress
			print( i, count_better, t,  best, best_eval, ' * if best ')

			count_better +=1

		# difference between candidate and current point evaluation
		diff = candidate_eval - curr_eval
		# calculate temperature for current epoch
		t = temp / float(i + 1)
		# calculate metropolis acceptance criterion
		metropolis = exp(-diff / t)

		# check if we should keep the new point
		if diff < 0 or rand() < metropolis:
			# store the new current point
			curr, curr_eval = candidate, candidate_eval
			print( i, count_weaker, best, best_eval, t, diff, metropolis, ' accept weaker solution')

			count_weaker +=1

	print(count_better, count_weaker, ' counts')
 


	return [best, best_eval]

# seed the pseudorandom number generator
seed(1)
# define range for input
bounds = asarray([[-5.0, 5.0]])
# define the total iterations
n_iterations = 1000
# define the maximum step size
step_size = 0.1
# initial temperature
temp = 10
# perform the simulated annealing search
best, score = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Done!')
print('f(%s) = %f' % (best, score))
