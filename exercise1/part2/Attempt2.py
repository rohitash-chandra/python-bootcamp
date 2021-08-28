import numpy as np

def right_tri():
    print('Right triangle printer')
    base = int(input('Please enter a non-negative integer value n: '))
    print('*')
    for i in range(base-1):
        print('*', end = '')
        for j in range(1,i+1):
            print(' ', end = '')
        print('*')
    for i in range(base+1):
        print('*', end = '')
    print()

def isos_tri():
    print('Isosceles triangle printer')
    base = int(input('Please enter a non-negative integer value n: '))
    for i in range(base):
        print(' ', end = '')
    print('*')
    for i in range(1, base):
        for j in range(base-i):
            print(' ', end = '')
        print('*', end = '')
        for j in range(1, 2*i):
            print(' ', end = '')
        print('*')
    for i in range(2*base):
        print('*', end = '')
    print('*')

def sin_plot(k, a, b):
    x_val = np.arange(k*a, k*b+0.1, 0.1*k)
    y_val = np.sin(x_val).round(1)
    print('I', end = '')
    for j in range(1, int(10+10*y_val[0])):
        print('-', end = '')
    print('*', end = '')
    for k in range(1, int(10-10*y_val[0])):
        print('-', end = '')
    print('I')
    for i in range(1, len(y_val)):
        if y_val[i] < 0:
            for j in range(int(10+10*y_val[i])):
                print(' ', end = '')
            print('*', end = '')
            for k in range(1, int(-10*y_val[i])):
                print(' ', end = '')
            print('I')
        else:
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