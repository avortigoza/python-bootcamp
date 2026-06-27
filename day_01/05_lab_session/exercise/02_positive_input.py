ask = True
while ask:
    try:
        number = int(input("Enter number: "))
        print(number)
        if number < 0:
            raise ValueError
        ask = False
    except ValueError:
        print("Enter a valid number!")