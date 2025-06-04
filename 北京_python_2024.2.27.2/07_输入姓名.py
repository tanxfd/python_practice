
i = 0
name_list = []

while i < 3:
    name = input("第" + str(i + 1) + "个名字：")
    if 2 <= len(name) <= 10:
        name_list.append(name)
    i += 1
    while i == 3:
        print(*name_list)
        i += 1

