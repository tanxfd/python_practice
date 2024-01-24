import random
import time

#先创建购物清单    #跟优惠券数量一样吧

shop_list = [['电视', 2000], ['电脑', 5000], ['冰箱', 1000], ['外套', 1600], ['挎包', 500],
             ['T恤', 90], ['小型工艺品', 50], ['戒指', 3000], ['空调', 1500], ['手机', 6000]]

#优惠券的列表     #要求必须有10种
discount_list = [['电视', 1500], ['电脑', 4500], ['冰箱', 800], ['外套', 1140], ['挎包', 450],
             ['T恤', 45], ['小型工艺品', 40], ['戒指', 2100], ['空调', 1200], ['手机', 4800]]

#购物商品清单，程序开始时为空集
cart_list: list[str] = []

rand = random.randint(0, 9)

#抽到哪张购物券就把优惠后的价格替换到原来的购物清单里
def __discount__(shop_list, discount_list, rand):
    shop_list[rand] = discount_list[rand]
    return shop_list

print("购物系统启动")

print("当前购物清单为")

print(shop_list)

print("恭喜你，你抽中了" + str(rand + 1) + "号优惠券")

print("现在的购物清单更新为")

shop_list = __discount__(shop_list, discount_list, rand)

print(shop_list)

card_money = input("你带了多少钱？")
shop_money = 0
shop_count = 0
start_time = time.perf_counter()
while True:         #购物开始
    print("你想要买点什么？")
    print(card_money)
    goods1 = input()
    if any(item[0] == goods1 for item in shop_list):
        if float(card_money) >= next((item[1] for item in shop_list if item[0] == goods1), None):
            cart_list.append(goods1)
            goods_money = next((item[1] for item in shop_list if item[0] == goods1), None)
            card_money = float(card_money) - goods_money
            shop_money = float(shop_money) + goods_money
            shop_count = shop_count + 1
            print("本次购物花费" + str(shop_money) + ",您的卡里还剩" + str(card_money))
        else:
            print("您的钱不够")
    print("您已经完成了一次购物，下列是您已购的物品")
    print(cart_list)
    sale_return = input("您是否需要退货?(yse/no或者quit退出)")
    if sale_return == 'yes':
        print("请输入你要退货的商品")
        goods2 = input()
        if goods2 in cart_list:
            cart_list.remove(goods2)
            goods_money = next((item[1] for item in shop_list if item[0] == goods2), None)
            card_money = float(card_money) + goods_money
            shop_money = float(shop_money) - goods_money
            shop_count = shop_count - 1
        else:
            print("您的购物车中没有该商品")
    elif sale_return == 'no':
        print("好的，您可以继续购物")
    elif sale_return == 'quit':
        print("好的，再见")
        end_time = time.perf_counter()
        break
    else:
        print("抱歉，我没明白您的意思(请输入yse/no)")

print("购物已结束，以下为您的购物回票")

print("您的购物清单为")
for i in cart_list:
    print(i)

print("您的购物时间为" + str(end_time - start_time) + ",卡余额为" + str(card_money)
      + ", 购买总价格为" + str(shop_money) + "购买的商品数为" + str(shop_count))
