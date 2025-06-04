import random

random_list = []
count = 0

for i in range(10):
    random_list.append(random.randint(0, 10))

print(random_list)

for i in random_list:
    count += i

print(count)

