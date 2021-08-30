
# Python Program to find the L.C.M. of two input number

# Source https://www.programiz.com/python-programming/examples/lcm

#The least common multiple (L.C.M.) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.

#For example, the L.C.M. of 12 and 14 is 84.

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))



#The above program is slower to run. We can make it more efficient by using the fact that the product of
 #two numbers is equal to the product of the least common multiple and greatest common divisor of those two numbers.

#Number1 * Number2 = L.C.M. * G.C.D.


# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))
