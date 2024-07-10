password = 12345 #integer
username = 'Sam'
user_name = input("Username: ")
user_pass = int(input("Password: "))

#austin_is_cool = False
#austin_is_bad = True
if user_pass == password and user_name == username:
    print("You logged in!")
    logged_in = True
else:
    print("Incorrect!")
    logged_in = False

if logged_in:
    choice = input("Withdraw (w) or Deposit (d): ")
    

else:
    print("You did not log-in")
