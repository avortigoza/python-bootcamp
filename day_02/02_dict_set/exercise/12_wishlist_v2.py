# TODO: Fill in the details of the items you plan to buy
order = [
    {
        "Name": "MacBook Pro",
        "Price": "120,000"
    },
    {
        "Name": "iPhone 17 Pro Max",
        "Price": "89,000"
    },
]

for print_details in order:
    print("Order: ")

    for key, value in print_details.items():
        print(f"\t {key}: {value}")

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
