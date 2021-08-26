

side = int(input("Please Enter any Side of a Square  : "))

print("Square Star Pattern - Nested For loops") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()
 
i = 0
print("Square Star Pattern - Nested While Loops") 

while(i < side):
    j = 0
    while(j < side):      
        j = j + 1
        print('*', end = '  ')
    i = i + 1
    print('')


m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end='')
    print()



m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [j, m-1] or j == 0 else ' ', end='')
    print()

