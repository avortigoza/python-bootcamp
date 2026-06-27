# TODO: Ask the user how many items will be calculated
quantity = int(input("How many items will be calculated? "))
input_count = 0
total = 0

# TODO: Use a for loop to ask for more than one cost and count
for item in range(quantity):
    item_cost = int(input("How much is the item? "))
    item_count = int(input("Enter the quantity of the item: "))
    item_total = item_cost * item_count
    total += item_total # total = total + item_total
print()
print(f"The total sales is {total}.")
