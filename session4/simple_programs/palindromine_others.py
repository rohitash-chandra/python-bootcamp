
#Source: https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/


# Python program to check
# if a string is palindrome
# or not
 
x = "malayalam movies"
 
w = ""
for i in x:
    w = i + w
    print(w, ' *')
 
if (x == w):
    print("Yes")
else:
    print("No")
   

# Python program to check
# if a string is palindrome
# or not
st = 'tennnxnnet'
j = -1
flag = 0
for i in st:
    print(i, st[j], '   *** ')

    if i != st[j]:
      j = j - 1
      flag = 1
      break
    j = j - 1
if flag == 1:
    print("NO")
else:
    print("Yes")


# Recursive function to check if a
# string is palindrome
 
def isPalindrome(s):
       
    #to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
     
    # if length is less than 2
    if l < 2:
        return True
 
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
        
        # Call is pallindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
 
    else:
        return False
 
# Driver Code
s = "MalaYaLam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
 
else:
    print("No")




# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "foolish"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")




