
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

    def distance(self, route):
        # sequentially calculate distance between all tsp nodes
        dist = 0
        for i in range(len(route)-1): 
            current = route[i]
            next = route[i+1]
            print(current, next, dist, ' *  ')
            dist += self.graph[current, next]
        return dist

    def generate_route(self):
        # ensure that route is corrent - one city can be visted only once!

        # route = [1,2,3,0] - corrent
        # route = [1,2,3,2] - not correct - vising city 2 again!


 
    def sim_annealing(self):

        route = [1,2,3,0]

        #route_coordinates = [1,2,3,4,2,4,1,3]

        dist = self.distance(route)

        print(route, dist, ' route dist')




#main

graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
     

mytsp = tsp(graph, 4)
mytsp.print_tsp()
mytsp.sim_annealing()


















