itemlist = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']           
itemcost = [0.75, 1.20, 1.20, 1.00, 1.50, 0.95, 1.10, 0.50, 1.20]
denomination = [1, 0.5, 0.2, 0.1, 0.05]
init_coins = 10
no_stocked = 10
coins = [init_coins]*len(denomination)                              #Global variable of the amount of coins left. Changes when purchases made. Resets with maintenance.
stock = [no_stocked]*len(itemlist)                                  #Global variable of the amount of remaining stock. Decreases when purchases made. Resets with maintenance.

#Process:
#1. Print Menu
#2. Ask to select items multiple times. On first attempt can quit or perform maintenance
#3. Check if order is above limit, otherwise go to payment
#4. Ask for coin input. These are counted and added to the coin pool. Items are reduced from the stock pool
#5. Return change if necessary
#6. Repeat

def ShowMenu():
    print('Vending Machine')
    print('+-------------+-------------+-------------+')
    print('|    Water    |     Coke    |  Diet Coke  |')
    print('|    $0.75    |    $1.20    |    $1.20    |')
    print('|     A1      |     A2      |     A3      |')
    print('+-------------+-------------+-------------+')
    print('|  Iced Tea   |  Chocolate  |    Candy    |')
    print('|    $1.00    |    $1.50    |    $0.95    |')
    print('|     B1      |     B2      |     B3      |')
    print('+-------------+-------------+-------------+')
    print('|    Chips    |     Gum     |Turk. Delight|')
    print('|    $1.10    |    $0.50    |    $1.20    |')
    print('|     C1      |     C2      |     C3      |')
    print('+-------------+-------------+-------------+')
    print('|        +----------------------+         |')
    print('|        |                      |         |')
    print('|        +----------------------+         |')
    print('+-----------------------------------------+')



def SalesSummary():
    sold = [None]*len(stock)
    for i in range(len(stock)):
        sold[i] = no_stocked - stock[i]                         #Calculate missing stock
        print('Sold', sold[i], 'units of', itemlist[i])
        stock[i] = no_stocked                                   #Reset stock levels in same loop
    balance = 0
    for i in range(len(denomination)):
        balance += coins[i] * denomination[i]                   #Calculate money in the machine
        coins[i] = init_coins                                   #Reset number of coins
    print('There is a balance of', balance)
    income = 0
    for i in range(len(itemcost)):
        income += sold[i] * itemcost[i]                         #Calculate total income
    print('Total income of $', income)
    input('Press the enter key to continue: ')
    ShowMenu()
    

def Payment(order):
    sales = []
    for item in itemlist:
        sales.append(order.count(item))                         #Count number of times each item appears in list typos not counted
    total = 0
    for i in range(8):
        total += sales[i]*itemcost[i]                           #Total cost of selection
    return sales, total

def MakeSelection(order):
    if len(order) == 0:                                                                             #Displays only on first run to quit or maintenance
        selection = input('Please select a product by typing its code or enter q to quit: ') 
        if selection == 'q':                                                                        #Stop if quit
            return 'quit'
        if selection == '99':                                                                       #Maintenance password
            code = input('*') #Super secret pin code
            if code == 'password':
                SalesSummary()
            else:
                MakeSelection(order)                                                                #Return if password is incorrect
        else:
            order.append(selection)                                                                 #I'm going to assume they type the codes correctly
    print('Your current order is: ', order)                                                         #Display current order and ask for additional orders
    additional = input('Type another code to add to your order or enter n to proceed to payment: ')
    if additional != 'n':                                                                           #Output order for payment
        order.append(additional)                                                                    #Run order process again
        MakeSelection(order)
    return order


def ReturnChange(owe, coins):
    for i in range(len(coins)):
        num = 0
        num = min(coins[i], round(owe, 2)//denomination[i])                         #Returns as many high denominations as possible. Limited by number of coins left
        if num > 0:
            print('Change owed:', round(owe,2))                                     #Python has strange rounding errors
            print('*The machine spits out', num, denomination[i], 'piece(s)')
        owe -= num*denomination[i]
    print('Thanks for using the vending machine.')



def DisplayErrorMessage(sales, total, stock, coins):
    for i in range(len(sales)):
        if sales[i] > stock[i]:                                                     #Check if sufficient stock
            print('Insufficient stock on product', sales[i], 'please reduce amount by', sales[i]-stock[i], 'units.')
            print('Order resetting...')
            MakeSelection([])                                                       #Clears current order to try again
    print('Your total is $', total)                                                 #If successful, count amount owed
    amount = 0
    while True:
        try:
            coin = float(input('Insert (by typing) each coin: '))
            ind = denomination.index(coin)                                          #Determine if correct denomination entered
        except ValueError:
            print('Invalid coin')
        else:
            coins[ind] += 1                                                         #Add inserted coin to the coin pool
            amount += coin                                                          #Sum the total money inserted
            owe = round(total - amount, 2)
            if owe > 0:                                                             #Stop asking for money once there is enough money to pay
                print('Amount owing:', owe)
            else:
                for i in range(len(sales)):
                    stock[i] -= sales[i]                                            #Reduce stock by the number of items purchased
                    print('Processing order...')
                return -owe                                                         #Negative amount owed is the change required to be given
                break
    
    


def main(): 
    ShowMenu()
    ord = MakeSelection([])
    if ord != 'quit':
        sal, tot = Payment(ord)
        change = DisplayErrorMessage(sal, tot, stock, coins)
        ReturnChange(change, coins)
        main()

if __name__ == '__main__':
    main()