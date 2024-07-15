import random
firstnum = random.randint(1,10)
secondnum = random.randint(1,10)
oper = ["+","-","*","/"]
random_oper = random.choice(oper)

print("Round decimals answers to the nearest tenth")
print(firstnum, random_oper, secondnum, "= ?")
user_ans = float(input(":"))
if random_oper == "*":
    ans = firstnum * secondnum
elif random_oper == "+":
    ans = firstnum + secondnum
elif random_oper == "-":
    ans = firstnum - secondnum
elif random_oper == "/":
    ans = firstnum/secondnum

ans = round(ans,1)

if user_ans == ans:
    print("Correct!")
else:
    print("Wrong! Answer was", ans)
