import tkinter as tk
from tkinter import messagebox

#variables
password = "12345"
username = 'Sam'
logged_in = False
money = 1000

#button functions
def update():
    money_label.config(text="$"+str(money))

def login():
    global logged_in, password, username
    user_pass = password_entry.get()
    user_name = username_entry.get()
    if user_pass == password and user_name == username:
        messagebox.showinfo("Login", "Successfully logged in!")
        logged_in = True
    else:
        messagebox.showinfo("Login", "Failed to login!")

def deposit():
    global money
    if logged_in:
        deposit_amount = int(amount.get())
        messagebox.showinfo("Deposit", "Deposited $" +str(deposit_amount))
        money += deposit_amount
        update()
    else:
        messagebox.showinfo("Alert", "Not logged in")

def withdraw():
    global money
    if logged_in:
        withdraw_amount =int(amount.get())
        messagebox.showinfo("Deposit", "Deposited $" +str(withdraw_amount))
        money -= withdraw_amount
        update()
    else:
        messagebox.showinfo("Alert", "Not logged in")

#make the window/app
app = tk.Tk()
app.title("ATM")

#intro
intro = tk.Label(app,text="ATM Services Page", background="gray")
intro.pack(side=tk.TOP)


#frame bruh
login_menu = tk.Frame(app)
login_menu.pack()

#username label and entry
username_label = tk.Label(login_menu, text="username:")
username_label.grid(row=1,column=0)
username_entry = tk.Entry(login_menu)
username_entry.grid(row=1,column=1)

#password label and entry
password_label = tk.Label(login_menu, text="password:")
password_label.grid(row=2,column=0)
password_entry = tk.Entry(login_menu, show="*")
password_entry.grid(row=2,column=1)

#login button
login_button = tk.Button(login_menu, text="Login!", command=login)
login_button.grid(row=3, column=1)

atm_menu = tk.Frame(app,pady=20)
atm_menu.pack()

amount_label = tk.Label(atm_menu,text="$")
amount_label.grid(row=0, column=0)
amount = tk.Entry(atm_menu)
amount.grid(row=0, column=1)

deposit_button = tk.Button(atm_menu, text="Deposit", command=deposit)
withdraw_button = tk.Button(atm_menu, text="Withdraw", command=withdraw)
deposit_button.grid(row=1,column=0)
withdraw_button.grid(row=1,column=1)


money_label = tk.Label(app, text="$"+str(money))
money_label.pack(side="bottom")
#main loop
app.mainloop()



''' OLD CODE

user_name = input("Username: ")
user_pass = int(input("Password: "))

#austin_is_cool = False
#austin_is_bad = True

if logged_in:
    choice = input("Withdraw (w) or Deposit (d): ") #"w" or "d"

else:
    print("You did not log-in")

money = 1000
print("You have $" + str(money))
if choice == "d":
    amount = int(input("How much money?: "))
    money = money + amount
    #money += amount
else:
    amount = int(input("How much money?:"))
    money = money - amount
print("You have $", money, sep="")
'''

def whenclicked():
    content = Myentry.get()
    Mylabel.config(text="The content in the entry is: "+content)