import fm_record


def usr_system():
    print("1.查询所有 2.按条件查询")
    while True:
        i = int(input())
        if i == 1:
            if len(fm_record.record.__dict__) == 0:
                print("当前帐单为空")
            else:
                default_table = {0: 'ID', 1: '类别', 2: '账户', 3: '金额', 4: '时间', 5: '说明'}
                print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}".format(*default_table.values(), *default_table.keys()))
                for i in fm_record.Record_num:
                    print()
                    print(f'{fm_record.record.fid: <5}'
                          f'{fm_record.record.classes: <10}'
                          f'{fm_record.record.account: <10}'
                          f'{fm_record.record.money: <10}'
                          f'{fm_record.record.date: <10}'
                          f'{fm_record.record.explain: <10}')
        # elif i == 2:
        #
        # elif i == 0:
        #     print("系统已关闭")
        #     break
        # else:
        #     print("请输入正确的选项")


usr_system()
