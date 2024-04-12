
price = 50
amount = 0
coins = [5, 10, 25]

while amount < price:
    print(f"Amount Due: {price - amount}")

#get input for the user
    user_input = int(input("Insert Coin: "))
    if user_input in coins:
        amount += user_input

print(f"Change Owed: {amount - price}")

