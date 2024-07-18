fibo = [1,1]
n = int(input("repeat:"))
for i in range(n):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo)