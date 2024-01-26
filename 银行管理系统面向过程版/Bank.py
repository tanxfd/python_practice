import User


# 创建的各种函数

def print_line():
    global i
    for i in range(20):
        print("*", end=' ', )
    print('\n')


def print_space(n):
    global i
    for i in range(n):
        print(" ", end='')


def print_title():
    print("*", end='')
    print_space(9)
    print("中国农业银行账户管理系统", end='')
    print_space(9)
    print("*")


def print_body(n, str):
    print("*", end='')
    print_space(n)
    print(str, end='')
    print_space(n)
    print("*")


def print_body_all():
    print_body(17, '选项')
    print_body(16, '1.开户')
    print_body(16, '2.存钱')
    print_body(16, '3.取钱')
    print_body(16, '4.转账')
    print_body(16, '5.查询')
    print_body(16, '6.Bye')


def print_ATM():
    print_line()
    print_title()
    print_line()
    print_body_all()
    print_line()


def create_account(self):
    new_user = User.User
    new_user.generate_id(self)
    user_id = new_user.get_id(self)
    if user_id in Bank_account:
        print("该用户已创建")
        return 2
    elif len(Bank_account) >= 100:
        print("用户已满，无法创建新用户")
    else:
        new_user.set_name(self)
        new_user.generate_id(self)
        new_user.set_client_degree(self)
        new_user.set_passwd(self)
        new_user.set_locate(self)
        new_user.set_credit_bank(self)
        user_info = [new_user.get_name(self),
                     new_user.get_pass(self),
                     new_user.get_locate(self),
                     new_user.cardMoney,  # 注意：这里cardMoney还没有设置值
                     new_user.get_client_degree(self),
                     new_user.get_credit_bank(self)  # 可以直接访问，但通常我们会通过getter方法获取
                     ]
        User.account_user[new_user.get_id(self)] = user_info
        Bank_account.update({new_user.get_id(self): user_info})
        # print(Bank_account)
        print({new_user: user_id})
        return 1


def save_money(account, user_id):
    user = User.new_user
    # print(Bank_account)
    # print(account)
    if account.get(user_id) is not None:
        User.new_user.id = user_id
        save_money_amount = int(input("请输入您要存款的金额"))
        account[user_id][3] += save_money_amount
        print("您的帐户当前存款为", user.cardMoney)
        # print(Bank_account)
        # print(account)
    else:
        print("对不起没有找您的帐户，请问是否需要开户？")
        return False


def withdraw_money(account, user_id):
    user = User.new_user
    if account.get(user_id) is not None:
        User.new_user.id = user_id
        user_pass = input("请输入密码:")
        if user_pass != account[user_id][1]:
            print("您的密码错误，重新选择业务")
            return 2
        else:
            out_money_amount = int(input("请输入您要取款的金额"))
            user.cardMoney = account[user_id][3]
            if out_money_amount > account[user_id][3]:
                print("取款金额超出您的存款余额，已退出取钱业务", account[user_id][3])
                return 3
            else:
                user.cardMoney -= out_money_amount
                account[user_id][3] = user.cardMoney
                print("您已取出", out_money_amount, "元，当前余额为", account[user_id][3])
                # print(Bank_account)
                # print(account)
                return 0
    else:
        print("对不起没有找您的帐户")
        return 1


def exchange_money(account, out_id, in_id):
    user1 = User.new_user  # 这个是转出的账户
    user2 = User.new_user  # 这个是转入的账户
    if account.get(out_id) is not None and account.get(in_id) is not None:
        user1.id = out_id
        user2.id = in_id
        user_pass = input("请输入您的密码:")
        if user_pass != account[out_id][1]:
            print("你的密码错误，已结束转账业务")
            return 2
        else:
            out_money = int(input("请输入您要转出的金额"))
            if out_money > account[out_id][3]:
                print("您账户的余额不够，已结束转账业务")
                return 3
            else:
                in_money = out_money
                user1.cardMoney -= out_money
                user2.cardMoney += in_money
                account[out_id][3] = user1.cardMoney
                account[in_id][3] = user2.cardMoney
                print("您已向用户", in_id, "转账", out_money, "元")
                # print(Bank_account)
                # print(account)
                return 0
    elif account.get(out_id) is None:
        print("您的账户不存在，请重新选择业务")
        return 1
    elif account.get(in_id) is None:
        print("你要转入的用户不存在，请重新选择业务")
        return 1


def show_account(account, user_id):
    user = User.new_user
    if account.get(user_id) is not None:
        user.id = user_id
        user_pass = input("请输入您的密码:")
        if user_pass != account[user_id][1]:
            print("您的密码错误，重新选择业务")
            return False
        else:
            print(account[user_id])
            print("您的帐户信息已查询完毕")
    else:
        print("您的账户不存在")
        return False


Bank_account = {39052790: ['张三', '000000', '中国河南解放路1号', 100000, 1, '中国农业银行昌平沙河支行']}
Using_user = User.new_user

print_ATM()

while 1:

    i = int(input())

    if i == 1:
        create_account(self=Using_user)
    if i == 2:
        id = input("请输入您的帐号")
        save_money(Bank_account, user_id=int(id))
    if i == 3:
        id = input("请输入你的账号")
        withdraw_money(Bank_account, user_id=int(id))
    if i == 4:
        id1 = input("请输入您的帐户")
        id2 = input("请输入要转入的账户")
        exchange_money(Bank_account, out_id=int(id1), in_id=int(id2))
    if i == 5:
        id = input("请输入您的帐户")
        show_account(Bank_account, user_id=int(id))
    if i == 6:
        print("尊敬的用户，再见！")
        break

