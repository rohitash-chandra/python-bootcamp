
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
 
import numpy as np



class tsp():
    def __init__(self, graph, num_cities):
        self.route = []
        self.graph = graph
        self.num_cities = num_cities

    def print_tsp(self):
        print(self.graph)


    
    '''def dist(self, xy):
        # sequentially calculate distance between all tsp nodes
        dist = 0
        for i in range(len(xy)-1): 
            dist += self.dist_func(xy[i+1], xy[i])
 
        
        return dist'''



graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
     

mytsp = tsp(graph, 4)
mytsp.print_tsp()


















