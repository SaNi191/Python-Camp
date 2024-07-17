import random
def english_to_sl(word):
    new_word = ("S"+word[::-1]+"muel")
    return new_word

#explanation
print("My language is called Samenglish\nFirst, add S at the start of the word.\nThen we add muel to the end of the word.\nFinally, reverse the word.")
#all words will start with s and end with muel

color = ["\u001b[31m","\u001b[32m","\u001b[33m","\u001b[34m","\u001b[35m","\u001b[36m","\u001b[37m"]
reset = "\u001b[0m"
mystr = input("Enter a word: ").lower().split() 

tl_phrase = ""
for word in mystr:
    random_color = random.choice(color)
    tl_phrase += random_color + english_to_sl(word) +reset+ " "

print(tl_phrase)
