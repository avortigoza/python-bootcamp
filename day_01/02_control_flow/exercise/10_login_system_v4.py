# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
# First Approach
# if username_input == correct_username and password_input == correct_password:
#     print("Access Granted.")
# else:
#     print("Access Denied.")

# Second Approach
correct_given_username = username_input == correct_username
correct_given_password = password_input == correct_password

if correct_given_username and correct_given_password:
    print("Access Granted.")
else:
    print("Access Denied.")