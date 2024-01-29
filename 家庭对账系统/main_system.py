import admin_sys
import usr_sys

# 开始打印登陆页面


while True:
    count = 0
    while count <= 3:
        usr = input("登录用户")
        pwd = input("用户密码:")
        if usr == 'admin':
            while pwd == '123456':
                print("管理员登陆成功")
                admin_sys.root_admin()
                break
            else:
                print("密码错误")
                break
        elif usr == 'lisi':
            while pwd == '123456':
                print("用户登录成功")
                usr_sys.usr_system()
                break
            else:
                print("密码错误")
                break
        else:
            count += 1
            print("用户不存在")
    else:
        print("用户验证次数超过三次，已退出进程")
        break
