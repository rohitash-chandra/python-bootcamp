

# source: https://www.w3schools.com/python/python_for_loops.asp

# source: http://sandbox.mc.edu/~bennet/python/code/

# while loop 

print(' basic while loop ')

i = 1
while i < 6:
  print(i)
  i += 1


print( 'exit the loop when i is 3')

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1




print(' find the sum of all numbers stored in a list ')

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val
    print(sum, ' print sum')

print("The sum is", sum)



# for loop 

print( 'print each fruit in a fruit list ')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print(fruits)


print( ' exit the loop when x is "banana", but this time the break comes before the print')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)




# Powers of 2 (for no obvious reason)
power = 1
for y in range(0 ,21, 4):
    print("2 to the", y, "is", power)
    power = 2 * power
    
# Scanning a list.
fred = ['And', 'now', 'for', 'something', 'completely', 'different.'];
for i in range(0,len(fred),2):
    print(i, fred[i])



# The for loop goes through a list, like foreach in
# some other languages.  A useful construct.
for x in ['Bill', 'Alice', 'Joe', 'Sue' ]:
    print(x, 'likes jelly beans.')

# The range operator simply creates a list of numbers
# in the indicated range.  Note that the range ends
# before the second argument.
print(range(5, 10))

# Range works with for to create the traditional for loop.
for y in range(2, 10):
    print(y)

    
print()

for y in range(2, 10, 2):
    print(y,end=' ')
print()

for y in range(20, 10, -1):
    print(y,end=' ')
print()


