minimum_height = 138

# TODO: Ask the user for the following inputs
user_height = int(input("What is your height? "))

# TODO: Notify user if they can enter the ride
can_enter_ride = user_height >= minimum_height
print("Can enter the ride:", can_enter_ride)
print(f"Can enter the ride: {can_enter_ride}")