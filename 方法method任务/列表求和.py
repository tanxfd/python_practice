
my_str = input("输入列表，元素之间以空格隔开")
my_list = my_str.split(" ")


def list_add(my_list):
    count = 0
    for i in range(0, len(my_list)):
        my_list[i] = int(my_list[i])
        count += my_list[i]
    return count


print(list_add(my_list))

