
x = 0
n = 0
threshold = 33550336

while True:
    x = x + 2 ** n
    n = n + 1
    if x > threshold:
        print("The value of x is", x, "The value of n is:", n)
        break
