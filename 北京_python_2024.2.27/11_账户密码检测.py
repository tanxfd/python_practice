
uname = input("输入账号名").lower().strip()

passwd = input("输入密码")

if uname is None or passwd is None:
    print("用户名或密码不能为空")
elif uname == 'admin' and passwd == 'Abc123':
    print("登陆成功")
else:
    print("用户名或密码错误")

