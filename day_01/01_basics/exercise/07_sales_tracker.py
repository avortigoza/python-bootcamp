# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("How much is the first item? "))
item_count_1 = int(input("Enter the quantity of the first item: "))

item_cost_2 = int(input("How much is the second item? "))
item_count_2 = int(input("Enter the quantity of the second item: "))

item_cost_3 = int(input("How much is the third item? "))
item_count_3 = int(input("Enter the quantity of the third item: "))

# Calculate the total
total = ((item_cost_1 * item_count_1) + (item_cost_2 * item_count_2) + (item_cost_3 * item_count_3))

print()
print(f"Your total expenses is {total}.")