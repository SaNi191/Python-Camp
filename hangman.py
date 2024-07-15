import random
"""
___
  |
  |
\_O_/
  |
 /\\
 """


lives_list = [4, 8, 12]
difficulty = int(input("easy (0)/medium (1)/hard (2):"))
lives = lives_list[difficulty]

word_list = ["apple", "banana", "orange", "grape", "strawberry", "blackberry", "durian", "pineapple", "tomato", "potato", "celery", "cherry", "peach", "mango", "blueberry"]

word = random.choice(word_list)

display = ["_"]*len(word)
guessed = []
while lives != 0:
    guess = input("guess:")
    if guess in word:
        index = 0
        for letter in word:
            if letter == guess:
                display[index] = guess
            index+=1
    else:
        lives -=1
        print("wrong")
        guessed.append(guess)
    print("LIVES:", lives)
    print("Guessed:", guessed)
    print(display)
