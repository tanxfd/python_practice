# 列表查询

def get_data(lst, num):
    if len(lst) > num >= -(len(lst)):
        return lst[num]
    else:
        return -1


my_list = [215, 875, 415, 127]
print(get_data(my_list, -5))
