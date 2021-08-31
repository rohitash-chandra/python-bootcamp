# Python program to display the Fibonacci sequence
#https://www.programiz.com/python-programming/examples/fibonacci-recursion

#https://en.wikipedia.org/wiki/Fibonacci_number


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       #print(n-1, n-2, recur_fibo(n-1), recur_fibo(n-2), '*')
       return(recur_fibo(n-1) + recur_fibo(n-2))


#------------------------------



print(recur_fibo(10), ' is fib 5')




nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


