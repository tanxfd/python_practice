import math

print("（1）计算圆的面积")
print("（2）计算长方形面积")

i = int(input())

if i == 1:
    r = int(input("请输入半径:"))
    if r > 0:
        s = math.pi * r * r
        print("圆的面积为" + str(s))
    else:
        print("圆的半径必须大于0")

elif i == 2:
    a = int(input("输入长方形的长:"))
    b = int(input("输入长方形的宽:"))
    if a > 0 and b > 0:
        s = a * b
        print("长方形的面积为" + str(s))
    else:
        print("长方形的长和宽必须大于0")
