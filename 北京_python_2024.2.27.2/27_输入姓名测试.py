
name = "admin"

while 1:
    input_name = input("输入姓名")
    if input_name != name:
        print("姓名错误，请重新输入")
    elif input_name == name:
        print(input_name)
        break
    else:
        print("输入非法")


print("程序结束")
