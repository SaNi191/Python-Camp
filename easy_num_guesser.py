import random
random_number = random.randint(1,10)
user_guess = int(input("Guess: "))

if user_guess == random_number:
	print("You guessed right! You win!")
else: 
	print("You guessed wrong! You lose! "+ "The right answer was " + str(random_number))

