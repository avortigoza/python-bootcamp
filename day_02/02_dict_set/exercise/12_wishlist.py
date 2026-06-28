# TODO: Fill in the details of the item you plan to buy
item = {
    "Name": ": MacBook Pro",
    "Year": ": 2026",
    "Price": ": 120,000"
}

# TODO: Print the item details in the following format:
def print_details(order):
    for category, item_details in order.items():
        print(category, item_details)
print_details(item)
