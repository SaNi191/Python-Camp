import random
options = ["rock", 'paper', 'scissors']

best_out_of = int(input("Best out of: ")) 



threshold = best_out_of//2+1
wins = 0
losses = 0


while True:
    computer = random.choice(options)
    choice = input("rock\npaper\nscissors\nchoice:").lower()

    print("Computer choice:", computer)
    print("Your choice:", choice)
    if wins == threshold:
        print("You win best out of", best_out_of)
        break
    elif losses == threshold:
        print("You lose best out of", best_out_of)
        break
    if choice == computer:
        print("Tied!")
    elif (choice == "rock" and computer == "paper") or (choice == "paper" and computer == "scissors") or (choice == "scissors" and computer == "rock"):
        print("You lost!")
        losses += 1
    else:
        print("You won!")
        wins += 1
    print(wins, "/", best_out_of)