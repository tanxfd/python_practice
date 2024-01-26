
import random

# 在当前文件定义locate类
class locate:
    country = ''
    province = ''
    street = ''
    house = ''

    def get_country(self):
        self.country = input("请输入国家\n")
        return self.country

    def get_province(self):
        self.province = input("请输入省份\n")
        return self.province

    def get_street(self):
        self.street = input("请输入街道\n")
        return self.street

    def get_house(self):
        self.house = input("请输入门牌号\n")
        return self.house

    # def set_country(self):
    #     locate.country = self.country
    #
    # def set_province(self):
    #     locate.province = self.province
    #
    # def set_street(self):
    #     locate.street = self.street
    #
    # def set_house(self):
    #     locate.house = self.house




#这是User类
class User:
    id = ''
    clientDegree = 0
    _name = ''
    passwd = ''
    locate = None
    cardMoney = 0
    _creditBank = ''
    maxExchange = 0

    def __init__(self):
        self.id = ''
        self.clientDegree = 0
        self._name = ''
        self.passwd = ''
        self.locate = None
        self.cardMoney = 0
        self._creditBank = ''
        self.maxExchange = 0

    def generate_id(self):
        self.id = random.randint(10000000, 99999999)  # ID应该是唯一的，这里使用随机数生成

    def set_client_degree(self):
        while True:
            client_degree = input("选择银行账户类型:\n"
                                  "1.【金卡】：最大转账额为5万，转出最大5万，转入没限制\n"
                                  "2.【普通卡】：最大转账额为2万，转出最大2万，转入没限制\n")
            if int(client_degree) == 1:
                self.maxExchange = 50000
                self.clientDegree = 1
                return
            elif int(client_degree) == 2:
                self.maxExchange = 20000
                self.clientDegree = 2
                return
            else:
                print("请输入正确的账户类型")

    def set_name(self):
        self._name = input("请输入姓名: ")

    def set_passwd(self):
        while True:
            passwd = input("请设置一个六位数密码: ")
            if len(passwd) == 6:
                self.passwd = passwd
                return
            else:
                print("请重新输入一个六位数密码")

    def set_locate(self):
        user_locate = locate
        str_locate = user_locate.get_country(locate) + user_locate.get_province(locate) + \
                     user_locate.get_street(locate) + user_locate.get_house(locate)
        self.locate = str_locate

    def set_credit_bank(self):
        self._creditBank = "中国农业银行昌平沙河支行"

    def get_id(self):
        return self.id

    def get_name(self):
        return self._name

    def get_locate(self):
        return self.locate

    def get_credit_bank(self):
        return self._creditBank

    def get_client_degree(self):
        return self.clientDegree

    def get_pass(self):
        return self.passwd

    # 其他getter方法类似
    @property
    def creditBank(self):
        return self._creditBank

    @property
    def name(self):
        return self._name


# 创建一个account_user字典
account_user = {}

# 创建一个用户实例并设置其属性
new_user = User()


