total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        # TODO: Ask for number
        number = int(input("Enter a number: "))
        # TODO: Add that number to the total
        total += number # total = total + number
        # TODO: Print the current total
        print(total)
        pass
    if command == "sub":
        number = int(input("Enter a number: "))
        total -= number
        print(total)
        pass
    if command == "multiply":
        number = int(input("Enter a number: "))
        total *= number
        print(total)
    elif command == "exit":
        running = False
