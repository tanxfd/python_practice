
n = int(input("输入一个正整数"))
i = 1
fac = i

while i < n:
    i += 1
    fac *= i
    while i == n:
        print(fac)
        i += 1
