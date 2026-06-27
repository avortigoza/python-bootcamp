# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
given_username = username_input == correct_username
given_password = password_input == correct_password
given_admin_username = username_input == admin_username
given_admin_password = password_input == admin_password

if (given_username and given_password) or (given_admin_username and given_admin_password):
    print("Access Granted.")
else:
    print("Access Denied.")