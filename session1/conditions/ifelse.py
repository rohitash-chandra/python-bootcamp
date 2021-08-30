# If the number is positive, we print an appropriate message

num = -1
if num > 0:
    print(num, "is a positive number.")
else:
    print(' the number is negative')


print("This is always printed * .") 


num = 44

if num > 40 and num < 50:
    print(num, "is between 41 to 49.")





# --- lets see range of numbers (boundaries)



num = 10

if num >= 40 and num < 50:
    print(num, "is between 40 to 49.")

elif num >= 50 and num < 100:
    print(num, "is between 50 to 99.")

else:
    print(num, "is either less than 40 or greater than 99.")

