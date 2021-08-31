# Program to check Armstrong numbers in a certain interval

# https://www.programiz.com/python-programming/examples/armstrong-interval

# https://en.wikipedia.org/wiki/Narcissistic_number

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

#. ie. 153 = (1 ^ 3) + (5 ^ 3) + (3 ^ 3)   # 3 is num of digits (1124 num digits would be 4)

# 1124 = (1 ^ 4) + (1 ^ 4) + (2 ^ 4) + (4 ^ 4)
#       = 1 + 1 + 16 + 256
# = 18 + 256
# 274

lower = 1
upper = 2000




num = 153

temp = num  # temp is 153
order = len(str(num))
digit = temp % 10   # 3
print(order, digit, digit ** order, ' * *' )
temp //= 10   # temp = 15
print(temp, ' * * *' )


 
#order = len(str(num))
digit = temp % 10   # 5
print(order, digit, digit ** order, ' * *' )
temp //= 10    # 
print(temp, ' * * *' )



order = len(str(num))
digit = temp % 10
print(order, digit, digit ** order, ' * *' )
temp //= 10
print(temp, ' * * *' )

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
       #print(digit, sum, temp )

   if num == sum:
       print(num)



