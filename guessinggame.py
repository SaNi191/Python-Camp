import random #this is a module, do not worry about it yet
random_number = random.randint(1,10) #random number from 1-10
user_guess = int(input("Guess: ")) #lets user input guess
if random_number == user_guess: #checks if guess is right
    print("You win!") #if right, print the win message
else:
    print("You lose! The number was", str(random_number)) #if not, print the lose message