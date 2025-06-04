
a = int(input("输入整数"))
b = int(input("输入整数"))
c = int(input("输入整数"))

if a > 0 and b > 0 and 0 < c < a + b and a + c > b and b + c > a:
    if a == b or b == c or a == c:
        if a == b and b == c:
            print("这个三角形是等边三角形")
        else:
            print("这个三角形是等腰三角形")
    else:
        print("这个三角形是普通三角形")
