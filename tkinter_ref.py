import tkinter as tk

def translate():
    word = entry.get()
    secret_word = "S"+word[::-1]+"muel"   # simple transformation
    label.config(text=f"Secret Language: {secret_word}")

app = tk.Tk()
app.title("Samenglish")
app.geometry("300x300")
entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Translate", command=translate)
button.pack()

label = tk.Label(app, text="")
label.pack()

app.mainloop()
