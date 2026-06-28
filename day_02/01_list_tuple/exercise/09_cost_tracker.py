"""TODO: Add a new cost in expenses"""
def spend(expenses):
    expense = int(input("How much is the item? "))
    expenses.append(expense)

"""TODO: Remove the last cost added (if any)"""
def refund(expenses):
    expenses.pop(-1)

"""TODO: Print the current list of expenses and total"""
def show(expenses):
    print(expenses)

    add_expenses = sum(expenses)
    print(f"Your total expenses is {add_expenses}.")


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "exit":
            running = False
        else:
            print("spend, refund, show, or exit only.")


main()
