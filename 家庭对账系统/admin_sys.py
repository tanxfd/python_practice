import fm_record


def root_admin():
    print(fm_record.Record_dict)
    print("1.添加账务 2.编辑账务 3.删除帐务 4.查询账务 5.退出系统")
    while True:
        global i
        i = int(input("请输入要操作的功能序号[1-5]:"))
        if i == 1:
            update_info(fm_record.Record_num + 1)
            write_file()
            print("添加账务成功")
        if i == 2:
            update_or_delete(i)
            write_file()
        if i == 3:
            update_or_delete(i)
            write_file()
        if i == 4:
            default_table = {0: 'ID', 1: '类别', 2: '账户', 3: '金额', 4: '时间', 5: '说明'}
            print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}".format(*default_table.values(), *default_table.keys()))
            for i in fm_record.Record_dict:
                print(fm_record.Record_dict)  # 摆烂ing 还是看得懂的
        if i == 5:
            break


def update_or_delete(i):
    print("请输入要编辑账目的ID：")
    int_record_id = int(input())
    while int_record_id < fm_record.Record_num + 1:
        if i == 2:
            print("请输入更改后的内容:")
            update_info(int_record_id)
            return i == 1
        elif i == 3:
            fm_record.record.fid = str(int_record_id)
            del fm_record.Record_dict[fm_record.record.fid]
        write_file()
    else:
        print("输入的ID超过了账单的条目，当前ID最大值为", fm_record.Record_num)


def update_info(id):
    int_record = input("请输入账务信息：")
    infos = int_record.split()
    fm_record.record.fid = str(id)
    fm_record.Record_dict.update({fm_record.record.fid: infos})


def write_file():
    with open("Recording.txt", "w") as file:
        file.write(str(fm_record.Record_dict))


# root_admin()
# print(fm_record.Record_dict)
