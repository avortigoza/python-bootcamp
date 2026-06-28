orders = {}

order = input("Enter order: ")
while order:
    count = int(input("Enter how many: ")) # Key

    if order in orders:
        orders[order] += count # orders[order] = orders[order] + count
    else:
        orders[order] = count
    order = input("Enter order: ") # Value

print(orders)


