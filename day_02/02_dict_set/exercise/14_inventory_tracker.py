def add(inventory):
    name = input("Enter the item name: ")
    info = input("Enter the item info: ")
    stock = input("Enter the item quantity: ")

    new_item = {
        "name": name,
        "info": info,
        "stock": stock
    }

    inventory.append(new_item)
        # Ask for item name, info, and stock

        # Create a dictionary with key: name, info, stock
        # Add that dictionary to inventory


def remove(inventory):
    index = int(input("Enter item index: "))
    inventory.pop(index)


def read(inventory):
    index = int(input("Enter item index: "))
    print(inventory[index])


def show(inventory):
    for print_details in inventory:
        print("Order: ")

        for key, value in print_details.items():
            print(f"\t {key}: {value}")


def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            add(inventory)
        elif command == "remove":
            remove(inventory)
        elif command == "read":
            read(inventory)
        elif command == "show":
            show(inventory)
        elif command == "exit":
            running = False


main()
