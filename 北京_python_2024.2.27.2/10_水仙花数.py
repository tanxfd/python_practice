
i = 100
while i < 1000:
    if int(i / 100)**3 + int(i % 100 / 10)**3 + int(i % 10)**3 == i:
        print(i)
    i += 1

