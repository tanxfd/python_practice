import random

print("游戏开始！")
print("初始金币:5000")
g = 5000
turn = 1

while turn >= 1:
    n1 = random.randint(0, 1000)
    if g >= 0:
        num = input("请输入一个数字:")
        if num.isdigit():
            print("你输入的是:", num)
            if int(num) == n1:
                g = g + 3000
                print("当前金额为", g)
                break
            elif int(num) < n1:
                print("小了")
                g = g - 500
                print("当前金额为", g)
            elif int(num) > n1:
                print("大了")
                g = g - 500
                print("当前金额为", g)
        else:
            print("输入有误，请重新输入")
    else:
        break

print("金额不足，游戏结束")
