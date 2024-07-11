num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print("Select your operation: ")
print("Addition (+)")
print("Subtraction (-)")
print("Multiplication (*)")
print("Division (/)")
user_choice = input("Choice: ")
if user_choice == "+":
    ans = num1 + num2
elif user_choice == "-":
    ans = num1 - num2
elif user_choice == "*":
    ans = num1 * num2
else:
    ans = num1/num2
print(ans)
#int()