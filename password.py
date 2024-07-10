password = 12345 #integer
username = 'Sam'
user_name = input("Username: ")
user_pass = int(input("Password: "))


if user_pass == password and user_name == username:
    print("You logged in!")
else:
    print("Incorrect!")
