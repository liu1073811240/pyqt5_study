# -- coding: utf-8 --
# @Time : 2022/5/23 17:30
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : table_sort2.py
# @Software: PyCharm


import numpy as np
import xlrd
import xlwt

def get_lists():

    file_path = '各地住院清单识别（已优化）.xlsx'

    wb = xlrd.open_workbook(file_path)
    # 获取第一个表
    sheet1 = wb.sheet_by_index(0)

    # 总行数
    nrows = sheet1.nrows
    # 总列数
    ncols = sheet1.ncols

    lists = []
    for i in range(nrows):
        for j in range(ncols):
            value = sheet1.cell_value(i, j)

            if len(value) > 0:
                lists.append(value)

    # print(lists)

    return lists



