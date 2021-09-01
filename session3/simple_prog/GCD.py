#The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers 
#is the largest positive integer that perfectly divides the two given numbers. 

# https://www.programiz.com/python-programming/examples/hcf

#For example, the H.C.F of 12 and 14 is 2.
 
# Python program to find H.C.F of two numbers

# GCD of 24 and 6 
# 6 ?

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y  # in case of 24 and 6, 6 is smaller
    else:
        smaller = x
    for i in range(1, smaller+1):
        print(i, smaller)
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
            print(hcf, ' hcf ')
    return hcf





num1 = 24 
num2 = 6



hcf = compute_hcf(num1, num2)


print("The HCF is", hcf)


#In this algorithm, we divide the greater by smaller and take the remainder. 
#Now, divide the smaller by this remainder. Repeat until the remainder is 0.

#For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24. 
#The remainder is 6. Now, we divide 24 by 6 and the remainder is 0. Hence, 6 is the required H.C.F.
 
# Function to find HCF the Using Euclidian algorithm



def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)


print("The HCF is", hcf)
