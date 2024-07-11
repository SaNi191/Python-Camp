'''
myName = "Samuel"
# consonant is S so we take that and add it to the back; "S" is at position 0 in the string
#newName = myName[1:].capitalize() + myName[0].lower() + "ay"
newName = "amuel" + "s" + "ay"
#[1:] takes all the letters in "Samuel" except the letter in position 0
print(newName)
'''

vowels = "aeiou"
print("o" in vowels)
words = input("Turn to pig-latin: ").split(" ")
PLwords = list()
for word in words:
    print(word)
    if word[0] in vowels:
        PLwords.append(word + "way")
    else:
        #not a vowel
        c_chunk = ""
        i = 0
        while word[i] not in vowels:
            c_chunk+=word[i]

        PLwords.append(word[len(c_chunk):]+c_chunk+"ay")
for PLword in PLwords:
    print(PLword, end = " ")
