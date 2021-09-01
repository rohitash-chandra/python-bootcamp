import csv

with open('Kelvin Maze.csv') as csvfile:
    Maze = list(csv.reader(csvfile, delimiter = ','))

#Duplicate Maze for Solutions
Sol = Maze

# O represents obstacle
# U represents unchecked, open cell
# C represents checked path
# S represents start
# G represents goal
# A represents answer (for output purposes)


def find_path(x, y):
    if Maze[x][y] == 'O':
        return False
    if Maze[x][y] == 'C':
        return False
    if Maze[x][y] == 'G':
        print(x,y)
        return True
    Maze[x][y] = 'C'
    if find_path(x+1, y):       #prioritises down-up search before right-left
        print(x,y)
        Sol[x][y] = 'A'
        return True
    if find_path(x-1, y):
        print(x,y)
        Sol[x][y] = 'A'
        return True
    if find_path(x, y+1):
        print(x,y)
        Sol[x][y] = 'A'
        return True
    if find_path(x, y-1):
        print(x,y)
        Sol[x][y] = 'A'
        return True

for r in range(len(Maze)):
    if 'S' in Maze[r]:
        startx = r
        starty = Maze[r].index('S')

find_path(startx, starty)

with open('Kelvin Solution.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Sol)