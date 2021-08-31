# Python program to swap two variables

# Source: https://www.programiz.com/python-programming/examples/swap-variables

#x = 5
#y = 10

#To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values

#12
temp = x
#15
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
