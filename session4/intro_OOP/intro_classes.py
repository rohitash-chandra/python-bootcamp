# source: https://www.csdojo.io/class

#https://en.wikipedia.org/wiki/Class_(computer_programming)


class Robot:
    def __init__(self): # constructor
        self.name = ' '
        self.color = ' '
        self.weight = 0
        self.height = 0

    def introduce_self(self):
        print("My name is ", self.name,  self.color, self.weight, self.height  )

    def set_properties(self, name, color, weight, height):
        self.name = name
        self.color = color
        self.weight = weight
        self.height = height




def func_exam(self, name, color, weight):
    print(' not part of class')


#main 

r1 = Robot()
r1.introduce_self()

r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r1.introduce_self()

# next robot


r2 = Robot()
r2.set_properties('Rohit', ' brownish', 78, 178)
r2.introduce_self()



 
print( ' more advanced class ')

class RobotAdv:
    def __init__(self, name, color, weight): # constructor
        self.name = name
        self.color = color
        self.weight = weight
        self.hight = 10

    def introduce_self(self):
        print("My name is " + self.name)
 

 # main

r3 = RobotAdv("Tom", "red", 30)
r4 = RobotAdv("Jerry", "blue", 40)

r3.introduce_self()
r4.introduce_self()




class Square:
    def __init__(self,  color, length, width): # constructor
       
        self.color = color
        self.length = length
        self.width = width

    def introduce_square(self):
        print("My name is " + self.color, self.length, self.width)

    def calculate_area(self):
        area = self.width * self.length
        return area
 

 # main

s1 = Square("red", 10, 30)
s2 = Square("blue", 20, 25)

s1.introduce_square()
s2.introduce_square()

total_area = (s1.length * s1.width) + (s2.length + s2.width)

print(total_area, ' area of s1 and s2')


total_area = s1.calculate_area() + s2.calculate_area()


print(total_area, ' area of s1 and s2 - another way')
