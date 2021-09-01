# Function to convert decimal number
# to binary using recursion

#https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/

#https://en.wikipedia.org/wiki/Pingala

#https://www.ascii-code.com/

#https://www.mathsisfun.com/binary-number-system.html


'''Input : 7                                                         
Output :111

Input :10
Output :1010'''


'''Example -: 1011
1). Take modulo of given binary number with 10. 
    (1011 % 10 = 1)
2). Multiply rem with 2 raised to the power
    it's position from right end. 
    (1 * 2^0)
    Note that we start counting position with 0. 
3). Add result with previously generated result.
    decimal = decimal + (1 * 2^0)
4). Update binary number by dividing it by 10.
    (1011 / 10 = 101)
5). Keep repeating upper steps till binary > 0.

Final Conversion -: (1 * 2^3) + (0 * 2^2) +
                 (1 * 2^1) + (1 * 2^0) = 11 '''

#https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/

#https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python


def decimal_binary(num):  # using recursion
     
    if num >= 1:
        decimal_binary(num // 2) 
    print(num % 2, end = '')

# 9/2 = 4
# 9 % 2 = 1

# 4/2 = 2
# 4%2 = 0

# 2/2 = 1
# 2%2 = 0

# 1/2 = 0
# 1%2 = 1

# 1001


def decimal_binary_iter(num):

    x=num
    k=[]
    while (num>0):
        a=int(float(num%2))
        k.append(a)
        num=(num-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
        
    return string
        


def binary_decimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        print(dec, decimal, binary, ' * + ')
        i += 1
    print(decimal)   
     
#1001 = 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0


#octa decimal numbers (base 8)
#hex decimal (base 16)
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 9
     
    # Calling function
    decimal_binary(dec_val)

    print()

    binary = decimal_binary_iter(dec_val)




    print('The binary no. for %d is %s'%(dec_val, binary))

    print('now convet binary to decimal')

    binary_decimal(int(binary)) 


    binary_decimal(100111)

    # 1  1
    # 10 2
    # 100 4
    # 1000 ?
    # 100000  32



