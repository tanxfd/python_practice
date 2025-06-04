
passwd = '123456'
count = 0

while count < 3:
    int_pass = input("请输入密码")
    if int_pass == passwd:
        print("欢迎取款")
        break
    else:
        print("密码错误")
        count += 1
        if count > 2:
            print("已经输错3次，卡将被吞")
            break
