amount = 50
pay = 0
coins = [25, 10, 5]

while amount > 0:
    print("Amount Due:", amount)
    money = int(input("Insert Coins: "))
    if money in coins:
        pay += money
        amount -= money


if pay >= amount:
    print("Change Owed:", pay-50)
