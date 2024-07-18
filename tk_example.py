import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Widgets")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Add an entry field
entry = tk.Entry(root)
entry.pack()

# Add a button
def on_button_click():
    user_text = entry.get()
    label.config(text=f"Hello, {user_text}!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the main loop
root.mainloop()
