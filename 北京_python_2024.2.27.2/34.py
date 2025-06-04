
name_list = ['张三', '李四', '王五']


for i in name_list:
    while 1:
        int_name = input(f"输入第{name_list.index(i) + 1}个名字：")
        if int_name != i:
            print("输入错误")
            print(f"请重新输入输入第{name_list.index(i) + 1}个名字：")
        else:
            break


print(*name_list)
