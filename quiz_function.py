import random

num1 = str(random.randint(1,100))
num2 = str(random.randint(1,100))

oper = ["+", "-", "*", "/"]
score = 0

for i in range(10):
    random_oper = random.choice(oper)
    equation = num1 + random_oper + num2


    print(num1, random_oper, num2, "=?")
    user_input = float(input(":"))
    if user_input == round(eval(equation), 2):
        print("Correct!")
        score +=1
    else:
        print("Wrong!")
print("Your score: ", score, "/", 10, sep="")


