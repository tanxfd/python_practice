
def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

i = 1
while i:
    if Fibonacci(i) < 200:
        print(Fibonacci(i))
    else:
        break
    i += 1
