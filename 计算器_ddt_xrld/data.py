import xlrd


def int_data(filename):
    da = xlrd.open_workbook(filename, encoding_override='utf-8')
    table = da.sheet_by_name('减法')
    rows = table.nrows  # 行数
    cols = table.ncols - 3  # 列数
    data_list = []
    for i in range(1, rows):
        row_list = []
        t1 = table.row_values(i)
        if type(t1[0]) == str and type(t1[1]) == str:
            t1[0] = int(t1[0])
            t1[1] = int(t1[1])
        data_list.append(t1)
        for j in range(0, cols):
            t2 = table.col_values(j)
            if t2 is str:
                t2 = int(t2)
            row_list.append(t2)
    return data_list

