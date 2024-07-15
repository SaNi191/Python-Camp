import random
firstnum = random.randint(-246,1740)
secondnum = random.randint(-364,1670)
correct = firstnum + secondnum

print(firstnum, "+", secondnum, "= ?")
#write the code that takes the users answer using input() and save it as ans
ans = int(input("ans:"))
if ans == correct:
    #write the code for a correct answer (congratulate!)
    print("Correct! You win!")
else:
    #write the code for a wrong answer
    print("Incorrect! You lose!")