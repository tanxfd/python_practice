
str_list = ['zhSan', 'LISI', 'wAnGwU', 'Zhaoliu', 'tianqi']


for i in str_list:
    print(i.lower().capitalize(), end=' ')
print('\n')

#   列表推导式
print(*[i.lower().capitalize() for i in str_list])
