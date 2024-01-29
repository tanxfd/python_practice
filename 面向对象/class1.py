

class student:
    student_id = 0
    name = ''
    sex = ''
    height = 0.0
    weight = 0.0
    grade = 0.0
    address = ''
    phone = 0

    def __init__(self):
        self.student_id = 0
        self.name = ''
        self.sex = ''
        self.height = 0.0
        self.weight = 0.0
        self.grade = 0.0
        self.address = ''
        self.phone = 0

    def study(self, time):
        print(self.name, "已经学习", time, "小时了")
        print('\n')

    def play_game(self, game):
        print(self.name, "在玩", game)
        print('\n')

    def program(self, n):
        print(self.name, "写了", n, "行代码")
        print('\n')

    def add(self, i1, i2):
        print(self.name, "做加法", i1, "+", i2, "=", i1 + i2)
        print('\n')
        return i1 + i2


xiaoming = student()
xiaoming.name = '小明'
xiaoming.study(1)
xiaoming.play_game('GTA')
xiaoming.program(100)
xiaoming.add(1, 2)
