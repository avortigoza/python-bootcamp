# Ask the user for an input
running = True
while running:
    email_input = input("Enter your email address: ")

# TODO: If valid gmail address
    check = email_input.endswith("@gmail.com")
    if check:
        print("This is a valid gmail address.")
        running = False

    # TODO: Else
    else:
        print("This is NOT a valid gmail address.")

