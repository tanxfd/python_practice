import datetime


class fRecord:

    fid = ''
    classes = ''
    account = ''
    money = 0.0
    date = '1900-01-01'
    explain = ''

    def __init__(self):
        fid = 0
        classes = ''
        account = ''
        money = 0.0
        date = '1900-01-01'
        explain = ''

    def set_fid(self):
        f = len(self.__dict__)
        self.fid = str(f)

    def set_classed(self):
        self.classes = input("输入类别:")

    def set_account(self):
        i = input("请选择账户类型：1.现金；2.交通银行；3.工商银行；4.建设银行；5.农业银行:")
        while True:
            if i == 1:
                self.account = '现金'
            elif i == 2:
                self.account = '交通银行'
            elif i == 3:
                self.account = '工商银行'
            elif i == 4:
                self.account = '建设银行'
            elif i == 5:
                self.account = '农业银行'
            else:
                print("请输入正确的选项")

    def set_money(self):
        self.money = float(input("请输入金额"))

    def set_date(self):
        year = int(input("年份"))
        month = int(input("月份"))
        day = int(input("日期"))
        input_date = datetime.date.replace(datetime.date.today(), year, month, day)
        self.date = datetime.date.strftime(input_date, "%Y-%m-%d")

    def set_explain(self):
        self.explain = input()
        if self.explain == '':
            self.explain = '无'

    def get_fid(self):
        return self.fid

    def get_classes(self):
        return self.classes

    def get_account(self):
        return self.account

    def get_money(self):
        return self.money

    def get_date(self):
        return self.date

    def get_explain(self):
        return self.explain


record = fRecord()
Record_key = {record.fid}
Record_info = [record.classes,
               record.account,
               record.money,
               record.date,
               record.explain]
Record_dict = {}


# 为了防止系统关机后丢失数据，所以把数据存储在文件里
# 每次打开系统时把文件的内容读取到字典里（和字典的结构保持一致）
with open("Recording.txt", 'r') as file:
    content = file.read()
Record_dict = eval(content)
Record_num = len(Record_dict)
