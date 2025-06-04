
list = [1, 2, 3, 4]

for i in range(0, 3):
    print(f"{3 - i}->", end='')
    print(*list)
    i += 1
