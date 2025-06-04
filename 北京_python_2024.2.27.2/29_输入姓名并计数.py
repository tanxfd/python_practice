
count = 0
name = '张三'

while 1:
    int_name = input("输入姓名")
    if int_name != name:
        print("姓名错误")
        count += 1
        if count < 3:
            print(f"还剩{3 - count}次机会(输入错误3次程序自动退出)")
        else:
            break
    elif int_name == name:
        print(int_name)
        break
    else:
        print("输入非法")


