
def speed_function_simple(speed): # example of function with no return value
    if speed < 80:
        print(" speed is ok")
    else:
        print(" you. have to pay a fine")


def speed_function_advanced(speed, provisonal): # example of function with return value

    total_fine = 0

    print(provisonal, ' is provisional')
        
    if (speed < 80) :
        print(" speed is ok.") 

    elif ((speed >= 80) and (speed < 100)) and (provisonal==True):
        base_fine = 500
        speed_diff = speed - 80
        extra_fine = speed_diff * 10
        total_fine = extra_fine + base_fine 
        print(" fine of (Pro is True) ", total_fine)

    
    elif ((speed >= 80) and (speed < 100)) and (provisonal==False):
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


# adap it for fine system in your country of residence

 


def main():
    print("Check speed of a vehicle and give fine!")

    #speed = int(input("Enter speed in km/hr for simple function:  "))

    #speed_function_simple(speed)


    speed_adv = int(input("Enter speed in km/hr for advanced function:  "))


    licence = input("Are you having a provisional licence? ")

    if licence == 'yes' or licence == 'Yes':
        provisional = True
    else:
        provisional = False


    fine = speed_function_advanced(speed_adv, provisional)

    print('the fine returned to main is: ', fine, '  dollars')


if __name__ == '__main__':
    main()
