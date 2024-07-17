import tkinter as tk

def show_secret_language():
    word = entry.get()
    secret_word = ''.join(reversed(word))  # simple transformation
    label.config(text=f"Secret Language: {secret_word}")

root = tk.Tk()
root.title("Secret Language")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Translate", command=show_secret_language)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
