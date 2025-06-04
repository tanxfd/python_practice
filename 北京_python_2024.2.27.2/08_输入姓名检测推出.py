
i = 1
name_list = []

def input_name(n):
    while n:
        name = input("第" + str(n) + "个名字：")
        if 2 <= len(name) <= 10:
            name_list.append(name)
        n += 1
        print("是否继续输入？")
        while 1:
            user_input = input().lower()
            if user_input == 'y':
                break
            elif user_input == 'n':
                return name_list
            else:
                print("请输入正确的回答")


input_name(i)
print(*name_list)
