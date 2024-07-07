myName = "Samuel"
# consonant is S so we take that and add it to the back; "S" is at position 0 in the string
newName = myName[1:].capitalize() + myName[0].lower() + "ay"
#[1:] takes all the letters in "Samuel" except the letter in position 0
print(newName)

