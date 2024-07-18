import tkinter
def translate():
    name = word_entry.get().lower()
    piglatin = (name[1:] + name[0] + "ay").capitalize()
    tl_word_label.config(text=piglatin)

app = tkinter.Tk()
app.title("Translator")
app.columnconfigure((0,1),weight=1)
app.rowconfigure((0,1,2),weight=1)
word_entry = tkinter.Entry()
word_entry.grid(row=0,column=1, sticky="nswe")
tkinter.Label(app,text="Word to Translate:").grid(row=0,column=0)

translate_button = tkinter.Button(app,text="Translate!", command=translate)
translate_button.grid(row=1,column=0, sticky="nswe")
tl_word_label = tkinter.Label(app)
tl_word_label.grid(row=2, sticky="nswe")

app.mainloop()

