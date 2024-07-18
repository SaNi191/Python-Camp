import tkinter as tk
from tkinter import messagebox, simpledialog

# Dummy credentials
correct_username = 'Sam'
correct_password = '12345'

# Function to validate login
def validate_login(username, password):
    return username == correct_username and password == correct_password

# Function to open the Deposit/Withdraw window
def open_deposit_withdraw_window():
    # Create a new window
    dw_window = tk.Toplevel()
    dw_window.title("Deposit/Withdraw")
    
    # Add widgets to the new window
    tk.Label(dw_window, text="Choose an action:").pack(pady=10)
    
    tk.Button(dw_window, text="Deposit", command=lambda: perform_action("Deposit")).pack(pady=5)
    tk.Button(dw_window, text="Withdraw", command=lambda: perform_action("Withdraw")).pack(pady=5)
    
    tk.Label(dw_window, text="Current Balance:").pack(pady=10)
    balance_label = tk.Label(dw_window, text="$1000")
    balance_label.pack(pady=10)
    
    # Function to perform deposit/withdraw
    def perform_action(action):
        amount = tk.simpledialog.askinteger("Input", f"How much to {action.lower()}?")
        if amount is not None:
            balance = int(balance_label.cget("text").strip('$'))
            if action == "Deposit":
                balance += amount
            elif action == "Withdraw":
                balance -= amount
            balance_label.config(text=f"${balance}")

# Function to handle login
def handle_login():
    username = entry_username.get()
    password = entry_password.get()
    if validate_login(username, password):
        messagebox.showinfo("Login Success", "You have successfully logged in!")
        root.withdraw()  # Hide the login window
        open_deposit_withdraw_window()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

# Create the main login window
root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=handle_login).pack(pady=20)

root.mainloop()
