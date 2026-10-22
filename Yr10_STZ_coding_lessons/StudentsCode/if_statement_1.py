type = input("Would you like a sandwich or a wrap?")
price = 0
if type == "sandwich":
    price = price + 3.00
    crisps = input("Would you like crisps? (y/n)")
    drink = input("Would you like a drink? (y/n)")

    if crisps == "y":
        price = price + 1.50
    if drink == "y":
        price = price + 1.00
    print("The cost of the order is: $" + str(price))
elif type == "wrap":
    price = price + 4.00
    crisps = input("Would you like crisps? (y/n)")
    drink = input("Would you like a drink? (y/n)")

    if crisps == "y":
        price = price + 1.50
    if drink == "y":
        price = price + 1.00
    print("The cost of the order is: $" + str(price))
else:
    print("Please type 'sandwich' or 'wrap'")
