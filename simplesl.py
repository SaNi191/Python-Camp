print("My language is called Samenglish\nFirst, add S at the start of the word.\nThen we add muel to the end of the word.\nFinally, reverse the word.")
#all words will start with s and end with muel
mystr = input("Enter a word: ").lower()
newword = "S" + mystr + "muel"
print(newword[::-1])
