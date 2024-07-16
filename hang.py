import random
wordbank = ['the quick brown fox jumps over the lazy dog', 'ant','spider', 'oshawott', 'samuel', 'cat', 'dog', 'horse', 'bear', 'eagle', 'tiger', 'lion', 'wolf', 'cougar', 'austin','austin','austin','austin','austin','austin','austin', 'monkey', 'leopard', 'elephant', 'tardigrade', 'derek', 'cockroach', 'gorilla']
word = random.choice(wordbank)

difficulty = input()
if difficulty == "e":
    lives = 10
elif difficulty == "m":
    lives = 6
else:
    lives = 3


guessed = []
display = ["_"]*len(word)


while True:
    if lives == 0:
        print("You lose")
        break

    if "".join(display) == word:
        print("You win!")
        break

    guess = input("guess 0 to quit\nguess:")
    guessed.append(guess)
    #USE if ___ in ___: to check if the guess is correct

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    
    else:
        print("Incorrect")
        lives-=1

    if guess == "0":
        break
    print(" ".join(display))
    print("You have", lives,"lives left")