
def speed_function_simple(speed): # example of function with no return value
    if speed < 80:
        print(" speed is ok")
    else:
        print(" you. have to pay a fine")


def speed_function_advanced(speed): # example of function with return value

    total_fine = 0
        
    if (speed < 80):
        print(" speed is ok.")

    elif (speed >= 80) and (speed < 100):
        base_fine = 200
        speed_diff = speed - 80
        extra_fine = speed_diff * 10
        total_fine = extra_fine + base_fine 
        print(" fine of  ", total_fine)
    elif (speed >= 100) and (speed < 140):
        print(" fine of 600 AUD")
    else:
        print(" time to go to prison. ")

    return total_fine

 


def main():
    print("Check speed of a vehicle and give fine!")

    speed = int(input("Enter speed in km/hr for simple function:  "))

    speed_function_simple(speed)


    speed_adv = int(input("Enter speed in km/hr for advanced function:  "))

    fine = speed_function_advanced(speed_adv)

    print('the fine returned to main is: ', fine, '  dollars')


if __name__ == '__main__':
    main()
