
money = input("请输入您携带的金额")

shop_list = [['电视', 2000], ['电脑', 5000], ['冰箱', 1000], ['外套', 1600], ['挎包', 500], ['T恤', 90], ['小型工艺品', 50], ['戒指', 3000]]

cart_list = []

while 1:
    print("请输入要购买的商品:(按下q退出)")
    goods = input()
    if any(item[0] == goods for item in shop_list):
        if float(money) > next((item[1] for item in shop_list if item[0] == goods), None):
            cart_list.append(goods)
            money = float(money) - next((item[1] for item in shop_list if item[0] == goods), None)
            print("您的卡里还剩" + str(money))
        else:
            print("您的钱不够")
    elif goods == 'q':
        break
    else:
        print("没有您要的商品")

print("购买的物品有:")

for i in cart_list:
    print(i)
