
name = input("请输入你的姓名")
gender = input("请输入性别")
age = int(input("输入年龄"))
height = float(input("输入身高"))
weight = float(input("输入体重"))
address = input("输入住址")

mysql = "insert into users values(‘%s’, ‘%s’, %d, %f, %f, ‘%s’)"

print(mysql%(name, gender, age, height, weight, address))
