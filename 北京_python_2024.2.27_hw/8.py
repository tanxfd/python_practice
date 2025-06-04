
count = 0
thick = 0.01

while 1:
    if thick <= 8844430:
        thick *= 2
        count += 1
    else:
        break

print(thick)
print(count)
