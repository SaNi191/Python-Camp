import tkinter

def translate():
    words = entry.get().split()
    phrase = ""
    for word in words:
        phrase+= "S"+word[::-1].lower()+"muel " #the transformation

    label.config(text="Secret Language:"+ phrase, font=("Times New Roman",20))

app = tkinter.Tk()
app.title("Samenglish")
app.geometry("600x300")

tkinter.Label(app,text="English to Samenglish Translator" ,font=("Times New Roman",40),background="blue",fg="yellow").pack(side="top")
entry = tkinter.Entry(app, width=30,font=("Times New Roman",20))
entry.pack()


button = tkinter.Button(app, text="Translate", font=("Times New Roman",20), background= "green", fg="red", command=translate)

button.pack()

label = tkinter.Label(app, text="",font=("Times New Roman",20),background="blue",fg="yellow")
label.pack()

app.mainloop()
