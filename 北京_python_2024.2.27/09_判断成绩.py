
i = int(input("输入成绩"))

if 90 <= i <= 100:
    print("成绩为优")
elif 80 <= i < 90:
    print("成绩为良")
elif 60 <= i < 80:
    print("成绩为及格")
elif i < 60:
    print("成绩为不及格")
else:
    print("成绩不合法")
