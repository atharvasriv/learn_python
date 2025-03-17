print("Hello!")

item = input("Please enter the name of the item: ")
cost = float(input("Please enter the cost of the item: "))
quantity = int(input("Please enter the amount of the item: "))

total_cost = cost * quantity

print(f"You have decided to buy {quantity} units of {item}, costing a total of ${total_cost}.")