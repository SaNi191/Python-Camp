import random


characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pass_length = int(input("Insert desired password length: "))
#remember random.choice(characters)
mypass = ""

for i in range(pass_length):
    choice = random.choice(characters)
    mypass += choice
print(mypass)
