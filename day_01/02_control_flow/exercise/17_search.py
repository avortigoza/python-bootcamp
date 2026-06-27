items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    item = input("Enter an item: ")
    if item == item_to_find:
        print()
        print(f"You have found the item - {item_to_find}.")
        break
    pass
