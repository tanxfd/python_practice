#!bin/bash
# 实际上并没有

a, b, c, d = (input("输入四个整数").split())
a = int(a)
b = int(b)
c = int(c)
d = int(d)


def __add__(a, b, c, d):
    add = a + b + c + d
    return add

print(__add__(a, b, c, d))
