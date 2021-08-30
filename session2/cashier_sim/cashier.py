




amount = input("Enter the amount of change owed: ")
amount = int(amount)


num_coins = [0, 5, 5, 5]

coins = [25, 10, 5, 1]
results = []


for i in range(len(coins)):
    coin_nb = int(amount / coins[i])
    results.append(coin_nb)
    amount = amount - (coins[i] * coin_nb)  


 
for i in range(len(coins)):
    print(coins[i], ' cents: ',  results[i], ' times') 


for i in range(len(coins)):
    num_coins[i] = num_coins[i] - results[i]

print(num_coins, ' is num coins ')