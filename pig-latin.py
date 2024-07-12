'''
myName = "Samuel"
# consonant is S so we take that and add it to the back; "S" is at position 0 in the string
#newName = myName[1:].capitalize() + myName[0].lower() + "ay"
newName = "amuel" + "s" + "ay"
#[1:] takes all the letters in "Samuel" except the letter in position 0
print(newName)
'''

vowels = ["a","e","i","o","u"]

words = input("Turn to pig-latin: ").lower().split(" ")
print(words)
PLwords = list()
for word in words:
    print(word)
    if (word[0] in vowels):
        print("start")
        #add the word to your list
        PLwords.append(word + "way")
        print("done, 1")

    else:
        #not a vowel
        c_chunk = ""
        i = 0
        while word[i] not in vowels and word[i] != "y":
            c_chunk+=word[i]   
            print("c_chunk:",c_chunk)
            i+=1

        #add the word to your word list
        PLwords.append(word[len(c_chunk):]+c_chunk+"ay")

print("Translated sentence: ")
for PLword in PLwords:
    #for each word, print it out
    print(PLword, end = " ")
