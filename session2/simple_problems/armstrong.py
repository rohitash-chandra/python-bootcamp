# Program to check Armstrong numbers in a certain interval

# https://www.programiz.com/python-programming/examples/armstrong-interval

# https://en.wikipedia.org/wiki/Narcissistic_number

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.



lower = 153
upper = 154

# 10

# order is 2

#temp = 10

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
       print(digit, sum, temp )

   if num == sum:
       print(num)
