

'''
What is a Palindrome?
A palindrome is nothing but any number or a string which remains unaltered when reversed.

Example: 12321
Output: Yes, a Palindrome number

Example: RACECAR
Output: Yes, a Palindrome string

It is evident that letters form mirror images on reversal.

'''


#Source: https://www.edureka.co/blog/python-program-to-check-palindrome/


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    print(dig, rev, num, ' * ')
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")



string=input(("Enter a string:"))

print(string, ' is entered')

for i in range(0, len(string) ):
    print(i, string[i],  ' ***')

backwards = string

j = 0
for i in range(len(string)-1, 0, -1 ):
    #backwards[j] = string[i]
    print(i,j, string[i],   ' **')
    j+=1
 
print(' reverse of what you entered  ', string[::-1])
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")




#other ways 

# function to check string is
# palindrome or not
def isPalindrome(s):
     
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")

# main function
s = "tamil"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")






