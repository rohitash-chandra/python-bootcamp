



num_coins = [5, 1, 0, 5, 5, 5]

coins = [200, 100, 50, 20, 10, 5]
give_coins = [0, 0, 0, 0, 0, 0]


item_price = [75, 120, 120, 100, 150, 95, 110, 50, 120 ]
num_items  = [10, 10, 10, 10, 10, 10, 10, 10, 10 ] 
item_name = ['water', 'coke', 'diet coke', 'iced tea', 'swiss choc', 'candy', 'chips', 'bubble gum', 'turkish delight']

# global definitions

def print_confidentialinfor():

    print(num_coins, ' num coins')

    print(num_items, ' num items')


def show_menu(): # make this nice
    for i in range(len(num_items)):
        print(i+1, ':', item_name[i], ' | ', num_items[i], ' | ', item_price[i], ' cents') 

def make_selection():
    show_menu()
    # ask the user to enter items 
 
    selection = input(' select items by using item ID, eg. 1123 would mean 2 coke and 1 water ')
 
    selection = int(selection) 

    print(' confirming your selection: ', selection)

    sum_items = 0

    temp = selection
    while temp > 0:
        digit = temp % 10 
        sum_items += item_price[digit-1]
        temp //= 10
        print(digit,   item_price[digit], sum_items )
    print(sum_items, ' sum items')

    return sum_items



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



    print(' here is a list of items, including number of items and price ')


    total_cost = make_selection()

    cost = total_cost

    print("Pay :", cost  ) 
    
    change = get_money(cost)
    if change > 0:
        give_change(change)
        #update item list
        
        #total_cost = make_selection()

    else: 
        print(' you have not given enough')
 




if __name__ == '__main__':
    main()
