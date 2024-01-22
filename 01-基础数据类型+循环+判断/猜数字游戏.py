# ！因为不是在linux上写python就解释器了

import random

n1 = random.randint(0, 1000)

i = 1

while i == 1:
    num = input("请输入一个数字:")
    print("你输入的是:", num)
    if int(num) == n1:
        break
    elif int(num) < n1:
        print("小了")
    elif int(num) > n1:
        print("大了")
    else:print("输入有错误，请重试")

print("猜对了，游戏结束")