import random

print("初始金币:5000")
g = 5000
turn = 1


# 给游戏部分创建一个函数，之后引用就行了

def game(n1):
    g = 5000
    while g >= 0:
        print("请输入一个数字:")
        i1 = input()
        if i1.isdigit():
            print("你输入的是:", i1)
            if int(i1) == n1:
                g = g + 3000
                print("当前金额为", g)
                return g
            elif int(i1) < n1:
                print("小了")
                g = g - 500
                print("当前金额为", g)
            elif int(i1) > n1:
                print("大了")
                g = g - 500
                print("当前金额为", g)
        else:
            print("输入有误，请重新输入")
    pass


while turn >= 1:
    n1 = random.randint(0, 1000)
    if turn == 1:
        print("游戏开始！")
        game(n1)
        turn = turn + 1
    elif turn >= 2:
        print("是否继续游戏？(yes/no)")
        n3 = input()
        if n3 == 'yes':
            print("游戏继续")
            game(n1)
        elif n3 == 'no':
            print("已退出")
            break
        else:
            print("输入错误")
    else:
        break
