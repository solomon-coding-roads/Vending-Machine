import sys
import time
                            # stop code with x
total = 0
coin = 0
change = 0
price = 0
valid_coins = 10, 20, 50, 100
select_item = ""
true_item = ""
valid = True
loop = True

items = "cereal bar", "crisps", "bottled water", "chocolate bar"
item_prices = 50, 60, 80, 90

while True:                             #while loop == True: 
    valid = True 
    print(f"Items: {items[0]}, {items[1]}, {items[2]}, {items[3]}")
    select_item = input("select item: ")

    select_item = select_item.lower().replace(" ", "")      #preparing for incorrect inputs

    if select_item == items[0].replace(" ", ""):
        price = item_prices[0]
        true_item = items[0]
    elif select_item == items[1].replace(" ", ""):
        price = item_prices[1]
        true_item = items[1]
    elif select_item == items[2].replace(" ", ""):
        price = item_prices[2]
        true_item = items[2]
    elif select_item == items[3].replace(" ", ""):
        price = item_prices[3]
        true_item = items[3]
    elif select_item == "x":
        sys.exit()
    else:
        print("Invalid choice!")
        print("-" * 35)
        valid = False

    if valid == True:
        print(f"That is {price}p")
        print("-" * 35)
        print(f"Valid Coins: {valid_coins[0]}p, {valid_coins[1]}p, {valid_coins[2]}p, {valid_coins[3]}p")

        while total < price:
            coin = input("Input coin: ")
            try:                                               #to not crash code when value error
                if int(coin) == valid_coins[0]:
                    total = total + valid_coins[0]
                elif int(coin) == valid_coins[1]:
                    total = total + valid_coins[1]
                elif int(coin) == valid_coins[2]:
                    total = total + valid_coins[2]
                elif int(coin) == valid_coins[3]:
                    total = total + valid_coins[3]
                else:
                    print("Invalid coin!")
                    print(f"Valid Coins: {valid_coins[0]}p, {valid_coins[1]}p, {valid_coins[2]}p, {valid_coins[3]}p")
            except ValueError:
                if coin == "x":
                    if total != 0:
                          print(f"change: {total}p")
                    sys.exit()
                else:
                    print("Not a valid input, enter a coin!")

            print(f": {total}p")

            if total > price:
                change = total - price
                time.sleep(0.4)
                print(f"change: {change}p")

        time.sleep(0.2)
        print(f"Paid, {true_item} ejected")
        time.sleep(1)
        print("-" * 35)
        total = 0
        change = 0
        time.sleep(1)