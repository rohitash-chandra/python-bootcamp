print('Your name?')
name = input()
print('Your height (m)?')
height = input()
print('Your weight (kg)?')
weight = input()

def bmi (h,w):
    bmi = w/(h*h)
    if bmi < 18.5: 
        bmi_status = 'underweight'
    elif bmi >= 18.5 and bmi < 25: 
            bmi_status = 'normal'
    elif bmi >= 25 and bmi < 30: 
            bmi_status = 'overweight'
    elif bmi >= 30: 
            bmi_status = 'obese'
    return(bmi, bmi_status)

BMI, BMI_status = bmi(float(height), float(weight))

print('Hi ',name,'.')
print('Your height is ',height,' and weight is ',weight,'.')
print('Your BMI is ', BMI, ' and you are ', BMI_status,'.')