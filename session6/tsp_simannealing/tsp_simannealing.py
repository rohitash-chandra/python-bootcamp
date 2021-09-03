
'''
0)  # initialize
    t_current = t_start
    s_current = x0
    s_best = x0

1)  # main optimization loop
    while t_current > t_min
        1.A) generate neighbor candidate -> s_new
        1.B) if P(E(s_current), E(s_new), T) >= random(0,1)
            s_current = s_new
        1.C) if E(s_new) < E(s_best)
            s_best = s_new
        1.D) update t_current
      
2)  # end
    output results



'''

#https://nathanrooy.github.io/posts/2020-05-14/simulated-annealing-with-python/


class tsp():
    def __init__(self, dist_func, close_loop=True):
        self.dist_func = dist_func
        self.close_loop = close_loop
    
    def dist(self, xy):
        # sequentially calculate distance between all tsp nodes
        dist = 0
        for i in range(len(xy)-1): 
            dist += self.dist_func(xy[i+1], xy[i])

        # close the tsp loop by calculating the distance 
        # between the first and last points
        if self.close_loop:
            dist += self.dist_func(xy[0], xy[-1])
        
        return dist
    
    def run_tsp(self, xxx):
        # begin optimizing
self.step, self.accept = 1, 0
while self.step < self.step_max and self.t >= self.t_min:

    # get neighbor
    proposed_neighbor = self.get_neighbor()

    # check energy level of neighbor
    E_n = self.cost_func(proposed_neighbor)
    dE = E_n - self.current_energy
    
    # determine if we should accept the current neighbor
    if random() < self.safe_exp(-dE / self.t):
        self.current_energy = E_n
        self.current_state = proposed_neighbor[:]
        self.accept += 1
        
    # check if the current neighbor is best solution so far
    if E_n < self.best_energy:
        self.best_energy = E_n
        self.best_state = proposed_neighbor[:]
    
    # update some stuff
    self.t = self.update_t(self.step)
    self.step += 1
