
s = "hello,python and pycharm"

print(len(s), s.index('o'), s.index('py'), s.find('PY'))

s = "hello,python and pycharm"
search_char = 'o'

# 初始化起始搜索位置
start_index = 0

# 循环直到找不到更多的'o'
while True:
    # 从start_index开始搜索'o'的位置
    index = s.find(search_char, start_index)

    # 如果找不到'o'，则退出循环
    if index == -1:
        break

        # 打印找到的'o'的位置
    print(f"Found '{search_char}' at index: {index}")

    # 更新起始搜索位置，从下一个位置开始搜索
    start_index = index + 1