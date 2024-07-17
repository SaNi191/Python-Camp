n = int(input("enter num:"))
factorial = 1
for i in range(n):
    factorial *= (i+1)
print(n, "! : ",factorial, sep="")
