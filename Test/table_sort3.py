# -- coding: utf-8 --
# @Time : 2022/5/23 18:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : table_sort3.py
# @Software: PyCharm

import numpy as np
import xlrd
import xlwt

def merge_space():
    file_path2 = 'write_test2.xls'

    wb = xlrd.open_workbook(file_path2)
    # 获取第一个表
    sheet2 = wb.sheet_by_index(0)

    # 总行数
    nrows2 = sheet2.nrows
    # 总列数
    ncols2 = sheet2.ncols

    total_lists2 = []
    for i3 in range(nrows2):
        row_lists = []
        for j3 in range(ncols2):
            # cell_value方法取出第i行j列的数据
            value3 = sheet2.cell_value(i3, j3)
            # print(value)
            if len(value3) > 0:
                row_lists.append(value3)

        if len(row_lists) > 0:
            total_lists2.append(row_lists)

    # print(np.array(total_lists2))
    # exit()

    return total_lists2

def write_xls3(out_array_):
    # 写入excel

    wb_ = xlwt.Workbook()
    # 添加一个表
    ws = wb_.add_sheet('write_test3')

    for i2, line_data2 in enumerate(out_array_):
        for j2, col_data2 in enumerate(line_data2):

            if i2 < 1500:  # 取前面一千条数据
                ws.write(i2, j2, col_data2)  # 3个参数分别为行号，列号，和内容

    wb_.save('./write_test3.xls')

if __name__ == '__main__':
    # 合并空行
    total_lists2 = merge_space()
    write_xls3(total_lists2)