import tkinter

def translate():
    word = entry.get()
    secret_word = "S"+word[::-1].lower()+"muel"   # simple transformation
    label.config(text="Secret Language:"+ secret_word)

app = tkinter.Tk()
app.title("Samenglish")
app.geometry("300x300")
entry = tkinter.Entry(app, width=30)
entry.pack()


button = tkinter.Button(app, text="Translate", command=translate)
button.pack()

label = tkinter.Label(app, text="",font=100)
label.pack()

app.mainloop()
