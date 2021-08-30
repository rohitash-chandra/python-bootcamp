# Program to transpose a matrix using a nested loop

# https://www.programiz.com/python-programming/examples/transpose-matrix



X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

print(len(X), 'leng')

# iterate through rows
for i in range(len(X)):
    # 0 1 2
   # iterate through columns
   for j in range(len(X[0])):
       # 0 1
       result[j][i] = X[i][j]

for r in result:
   print(r)
