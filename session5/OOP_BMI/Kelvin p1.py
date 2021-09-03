from datetime import date
import numpy as np

def find_age():
    birthinput = input('Please enter your date of birth (DDMMYYYY): ')
    if len(birthinput) != 8:
        print('Entered date of birth invalid')
        find_age()
    else:
        today = date.today().strftime('%Y%m%d')
        birthdate = birthinput[4:9]+birthinput[2:4]+birthinput[0:2]             #Use YYYYMMDD to prioritise year, then month, then day
        age = int((int(today)-int(birthdate))/10000)                            #eg 20210101 - 20200101 = 10000 > 0 so 20210101 is a later date
        print('Your age is ', age, '.', end = ' ')
        if age > 18:
            print('Using adult BMI classification.')
        else:
            print('Using child BMI classification.')
        return age

def find_height():
    print('Would you like to input your height in metres, or feet and inches?')
    unit = input('Enter m for metres or f for feet and inches here: ')                                               #Ask for unit of input   
    if unit == 'm':
        height = float(input('Please enter your height in metres up to two decimal places. (eg. 1.78): '))
    elif unit == 'f':
        heightinput = input('Please enter your height in feet and nearest inch, separated by \'. (eg. 5\'7): ')      #Just going to trust they entered it correctly
        feet_inch = heightinput.split(sep = '\'')                                                                    #Find the ' and split the numbers into 2
        height = float(feet_inch[0])*0.3048 + float(feet_inch[1])*0.0254
    else:
        find_height()
    return height

def find_weight():
    weight = float(input('Please enter your weight in kg. (eg. 53): '))                                             #Also going to trust they entered a number
    return weight

def calc_BMI(weight, height):
    BMI = weight/height**2
    print('Your Body Mass Index is ', BMI)
    return BMI

def calc_class(BMI, age):
    adult_classes = np.array([16.00, 17.00, 18.50, 25.00, 30.00, 35.00, 40.00])             #Use elementwise comparison then count the number of True
    child_classes = np.array([20.00, 29.00, 32.00])
    if age > 18:
        group = sum(BMI > adult_classes)                                                    #How many cutoffs is the BMI greater than? ranges from 0 to 8 (9 choices)
        if group < 3:                                                                       #Main class
            print('Your classification is Underweight', end = ' ')
            if group == 0:                                                                  #Sub classes
                print('with subclassification Severe thinness.')
            elif group == 1:
                print('with subclassification Moderate thinness.')
            else:
                print('with subclassification Mild thinness.')
        elif group < 4:
            print('Your classification is Normal Range.')
        elif group < 5:
            print('Your classification is Overweight with subclassification Pre-obese.')
        else:
            print('Your classification is Overweight')
            print('You are also Obese', end = ' ')
            if group < 6:
                print('with subclassification Obese class I.')
            elif group < 7:
                print('with subclassification Obese class II.')
            else:
                print('with subclassification Obese class III.')
    else:
        group = sum(BMI > child_classes)
        if group == 0:
            print('Your classification is Underweight.')
        elif group == 1:
            print('Your classification is Healthy weight.')
        elif group == 2:
            print('Your classification is Overweight.')
        else:
            print('Your classification is Obese.')


        




def main(): 
    quit = input('Press the enter key to start or enter q to quit: ')
    if quit != 'q':
        print('BMI Calculator')
        age = find_age()
        height = find_height()
        weight = find_weight()
        BMI = calc_BMI(weight, height)
        calc_class(BMI, age)
        main()

if __name__ == '__main__':
    main()