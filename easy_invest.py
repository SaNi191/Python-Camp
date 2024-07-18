import random
turn = 0
stock_price = random.randint(10,150)
#adds 5 random prices representing 5 stocks
money = 100000
owned_stocks = 0
print("Welcome to \"Can you become a millionaire?!?\"")
def new_turn(): 
    global stock_price, turn, money
    networth = owned_stocks * stock_price + money
    turn+=1
    stock_price *= random.uniform(0.85,1.15)
    if networth >= 1000000:
        print("Congratulations! You are a millionaire!")
        return True
    return False

def buy_stocks():
    global stock_price, money, owned_stocks
    if money >= stock_price:
        print("You can buy ", money//stock_price, "stocks")
        amount = int(input("How many stocks would you like to buy?:"))
        if amount > money//stock_price:
            print("Invalid amount.")
        else:
            money -= (amount*stock_price)
            owned_stocks += amount
    else:
        print("You cannot afford any stocks")

def sell_stocks():
    global stock_price, owned_stocks, money
    print("You can sell", owned_stocks, "stocks")
    amount = int(input("How many would you like to sell?:"))
    if amount > owned_stocks:
        print("You cannot sell that many. Try again.")
    else:
        money += amount * stock_price
        owned_stocks -= amount

while True:
    print("0|See info\n1|New Turn\n2|Buy Stocks\n3|Sell Stocks\n4|Exit Game")
    choice = input(":")
    if choice == "0":
        print("money:",money,"\nowned stocks:",owned_stocks, "\nstock price:",stock_price)
    elif choice == "1":
        if new_turn():
            break
    elif choice == "2":
        buy_stocks()
    elif choice == "3":
        sell_stocks()
    else:
        input("Ending the game...")
        break 

print ("$",stock_price)

