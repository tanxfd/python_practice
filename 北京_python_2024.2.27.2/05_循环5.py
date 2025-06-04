
n = int(input("输入一个正整数"))
i = 1
sum = 0

while i < n:
    sum += i
    i += 1
    while i == n:
        sum += i
        print(sum)
        i += 1
