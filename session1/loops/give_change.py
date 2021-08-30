



#lets assume we have 50, 20, 10, 5 cents coin denominations

amount = 75

change = int(amount/50)  # 1.5   # 1 
amount = amount%50       #  25

print(change, amount)

change = int(amount/20)   #1.25  #  1
amount = amount%20        # 5

print(change, amount)

change = int(amount/10)  # 0.5   # 0
amount = amount%10    #  5

print(change, amount)


change = int(amount/5)  # 1
amount = amount%5    #  0

print(change, amount)




# you can use a while loop to make this automated. 

amount = 75

coins = [50, 20, 10, 5]
i = 0
while(amount!=0):
    change = int(amount/coins[i])
    amount = amount%coins[i]
    print(change, amount)
    i= i +1












amount = input("Enter the amount of change owed: ")
amount = int(amount)

coins = [25, 10, 5, 1]
results = []


for i in range(len(coins)):
    coin_nb = int(amount / coins[i])
    results.append(coin_nb)
    amount = amount - (coins[i] * coin_nb) # We substract the change we already gave back



print("Quarters: {}".format(results[0]))
print("Dimes: {}".format(results[1]))
print("Nickels: {}".format(results[2]))
print("Pennies: {}".format(results[3]))


# another way of printing 


for i in range(len(coins)):
    print(coins[i], ' cents: ',  results[i], ' times') 



# another way of doing the same


amount = input("Enter the amount of change owed: ")
amount = int(amount)

coins = [50, 20, 10, 5]
results = []


for coin in coins:  # another way to loop 
    coin_nb = int(amount / coin)
    results.append(coin_nb)
    amount = amount - (coin * coin_nb) # We substract the change we already gave back



print("50: {}".format(results[0]))
print("20: {}".format(results[1]))
print("10: {}".format(results[2]))
print("5: {}".format(results[3]))


# Can you use functions to do this?

# Can you use a stack of coins,  eg 10 coins of each denomination each ?

# Can you simulate an old cashier machine at the supermarket?
