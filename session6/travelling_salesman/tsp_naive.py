# Python3 program to implement traveling salesman
# problem using naive approach.

#Source https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/?ref=lbp


from sys import maxsize
from itertools import permutations
V = 4
 
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    print(vertex, ' is vertex')
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)




    for i in next_permutation:

         
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            print(k, j, current_pathweight, ' *')
            k = j
        current_pathweight += graph[k][s]

        print(i, current_pathweight, ' path and dist')
 
        # update minimum
        min_path = min(min_path, current_pathweight)
         
    return min_path
 
 
# Driver Code
if __name__ == "__main__":
 

 # 1 - 2 (10)  0 - 1 (10)   1 - 0 (10)
 # 1 - 3 (15)  0 - 2 (15)   2 - 0 (15)


    # matrix representation of graph
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
