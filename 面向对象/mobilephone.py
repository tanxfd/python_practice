import time


class people:
    name = ''
    sex = ''
    age = 0
    remain_charge = 0.0
    size = 0.0
    standby_time = 0.0
    score = 0

    # 不考虑什么发送了，直接print
    def send_mess(self, txt):
        print(txt)

    def call(self, number, time_count):
        if number is None:
            print("the number you call is None")
        elif self.remain_charge < 1:
            print("your phone charge is less then 1 yuan")
        else:
            if time_count < 10:
                self.remain_charge -= time_count
                self.score += 15 * time_count
            elif 10 <= time_count < 20:
                self.remain_charge -= 0.8 * time_count
                self.score += 39 * time_count
            else:
                self.remain_charge -= 0.65 * time_count
                self.score += 48 * time_count

