



num_coins = [5, 1, 0, 5, 5, 5]

coins = [200, 100, 50, 20, 10, 5]
give_coins = [0, 0, 0, 0, 0, 0]


item_price = [75, 120, 120, 100, 150, 95, 110, 50, 120 ]
num_items  = [10, 10, 10, 10, 10, 10, 10, 10, 10 ] 
item_name = ['coke', 'water']

# global definitions

def print_confidentialinfor():

    print(num_coins, ' num coins')

    print(num_items, ' num items')


def show_menu(): # make this nice
    
    print(item_name, ' item list')
    print(num_items, ' num items')
    print(item_price, ' num items')

def make_selection():
    show_menu()
    # ask the user to enter items 

    # 1123  
    #for or while using mod and div
    # 1 1 2 3 (index)

    # refr item list and price

    sum = 0
    #while loop or for loop
        #sum = sum +  item_price[index-1]


    return sum



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
