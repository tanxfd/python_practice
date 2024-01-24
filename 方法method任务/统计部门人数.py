

list_ceshi = ['小明', '小张', '小黄', '小杨']
list_yanfa = ['小黄', '小李', '小王', '小杨', '小周']
list_shichang = ['小杨', '小张', '小吴', '小冯', '小周']
set_company = set()

def sum_emp(list1, list2, list3):
    for item in list1:
        set_company.add(item)
    for item in list2:
        set_company.add(item)
    for item in list3:
        set_company.add(item)
    return len(set_company)


print(sum_emp(list_ceshi, list_yanfa, list_shichang))

