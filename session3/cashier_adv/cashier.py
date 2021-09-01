



num_coins = [5, 1, 0, 5, 5, 5]

coins = [200, 100, 50, 20, 10, 5]
give_coins = [0, 0, 0, 0, 0, 0]

# global definitions



def give_change(change): 

    for i in range(len(coins)):
        #print (num_coins[i], i, ' *')
        if num_coins[i] >0:
            coin_nb = int(change / coins[i])
            give_coins[i] += coin_nb 
            change = change - (coins[i] * coin_nb)  
        
    for i in range(len(coins)):
        print(coins[i], ' cents: ',  give_coins[i], ' times') 

    for i in range(len(coins)):
        num_coins[i] = num_coins[i] - give_coins[i]

    print(num_coins, ' is num coins ')

def get_money(cost):
    amount = input(' enter amount you have so we can give change :')
    amount = int(amount)
    change = amount - cost
    print('your  change is : ', change)
    return change



def main(): 

    print(' lets simulate a cashier machine ')
        
    # assune you selected items with following cost:
    cost = 75

    print("Pay :", cost  ) 
    
    change = get_money(cost)
    if change > 0:
        give_change(change)
    else: 
        print(' you have not given enough')
 




if __name__ == '__main__':
    main()
