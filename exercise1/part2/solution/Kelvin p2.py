import numpy as np

def right_tri():
    print('Right triangle printer')
    base = int(input('Please enter a non-negative integer value n: '))
    print('*')                                                          #Start of the triangle. Only line with one *
    for i in range(base-1):
        print('*', end = '')                                            #Prints the first * and sufficient number of spaces
        for j in range(1,i+1):
            print(' ', end = '')
        print('*')                                                      #Prints the second *
    for i in range(base+1):
        print('*', end = '')                                            #Prints the base of the triangle
    print()

def isos_tri():
    print('Isosceles triangle printer')
    base = int(input('Please enter a non-negative integer value n: '))
    for i in range(base):
        print(' ', end = '')                                            #Start by printing n spaces
    print('*')                                                          #First row has one *
    for i in range(1, base):
        for j in range(base-i):
            print(' ', end = '')                                        #Each subsequent row has n-i spaces
        print('*', end = '')                                            #Then two * separated by enough spaces
        for j in range(1, 2*i):
            print(' ', end = '')
        print('*')
    for i in range(2*base):
        print('*', end = '')                                            #Base is 2*n+1
    print('*')

def sin_plot(k, a, b):
    x_val = np.arange(k*a, k*b+0.1, 0.1*k)                              #Calculate the x values - like linspace would on MATLAB
    y_val = np.sin(x_val).round(1)                                      #Calculate the y values - but round to the nearest 0.1 to plot
    print('I', end = '')
    for j in range(1, int(10+10*y_val[0])):
        print('-', end = '')                                            #First row has the -
    print('*', end = '')                                                #But also has *
    for k in range(1, int(10-10*y_val[0])):
        print('-', end = '')                                            #Then fill the rest with -
    print('I')
    for i in range(1, len(y_val)):
        if y_val[i] < 0:                                                #If negative value, * comes before I
            for j in range(int(10+10*y_val[i])):
                print(' ', end = '')                                    #Put enough spaces before the *
            print('*', end = '')
            for k in range(1, int(-10*y_val[i])):
                print(' ', end = '')
            print('I')
        else:                                                           #If positive value, I comes before *
            for k in range(10):
                print(' ', end = '')
            print('I', end = '')
            for j in range(1, int(10*y_val[i])):
                print(' ', end = '')
            print('*')


def main():
    right_tri()
    isos_tri()
    sin_plot(3, 0, 3.1)

if __name__ == '__main__':
    main()