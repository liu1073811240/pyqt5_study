# -- coding: utf-8 --
# @Time : 2022/5/23 16:30
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : table_sort.py
# @Software: PyCharm
import numpy as np
import xlrd
import xlwt
from table_sort2 import get_lists

file_path = 'test.xlsx'

wb = xlrd.open_workbook(file_path)
# 获取第一个表
sheet1 = wb.sheet_by_index(0)

# 总行数
nrows = sheet1.nrows
# 总列数
ncols = sheet1.ncols

# 后面就通过循环即可遍历数据了
# 取数据
total_lists = []
total_num = []
for i in range(nrows):
    line_list = []
    for j in range(ncols):
        # cell_value方法取出第i行j列的数据
        value = sheet1.cell_value(i, j)
        # print(value)
        line_list.append(value)

        if j == 3:
            total_num.append(int(value))

    total_lists.append(line_list)

total_array = np.array(total_lists)
# print(total_array)
# print(total_num)

indexed_num = np.argsort(-np.array(total_num))  # 降序排列
# print(indexed_num)

out_array = total_array[indexed_num]
# print(out_array)


def write_xls(out_array_):
    # 写入excel
    wb = xlwt.Workbook()
    # 添加一个表
    ws = wb.add_sheet('write_test1')
    for i_, line_data in enumerate(out_array_):
        for j_, col_data in enumerate(line_data):
            ws.write(i_, j_, col_data)  # 3个参数分别为行号，列号，和内容

    wb.save('./write_test.xls')

def write_xls2(out_array_):
    # 写入excel
    wb_ = xlwt.Workbook()
    # 添加一个表
    ws = wb_.add_sheet('write_test2')

    # filter_index_l = []
    # for i_, line_data in enumerate(out_array_):
    #     for j_, col_data in enumerate(line_data):
    #         # print(col_data)
    #         print(i_, j_)
    #         lists = get_lists()
    #         # print(lists)
    #         if col_data in lists:
    #             filter_index_l.append(i_)
    #             # ws.write(i_, j_, col_data)  # 3个参数分别为行号，列号，和内容
    # print(filter_index_l)

    filter_index_l2 = [7, 8, 11, 12, 15, 16, 18, 19, 23, 24, 29, 32, 33, 35, 36, 38, 40, 45, 47, 49, 50, 54, 55, 60, 61, 62, 70, 71, 78, 80, 86, 93, 94, 100, 101, 108, 109, 110, 120, 127, 132, 133, 136, 140, 152, 154, 155, 169, 170, 173, 174, 175, 177, 179, 182, 186, 193, 195, 196, 205, 209, 221, 222, 224, 229, 232, 233, 234, 235, 236, 258, 259, 260, 264, 269, 272, 278, 279, 280, 288, 289, 291, 294, 297, 299, 304, 308, 312, 319, 320, 326, 333, 335, 339, 342, 352, 355, 362, 364, 369, 370, 375, 378, 385, 391, 392, 397, 403, 407, 413, 419, 429, 430, 444, 445, 453, 469, 485, 501, 512, 516, 519, 538, 548, 568, 580, 590, 595, 609, 627, 630, 635, 649, 679, 684, 689, 690, 694, 712, 734, 746, 750, 752, 758, 769, 770, 771, 802, 815, 816, 840, 844, 848, 858, 860, 891, 914, 920, 945, 953, 957, 979, 998, 1004, 1034, 1041, 1070, 1082, 1131, 1153, 1161, 1165, 1186, 1196, 1266, 1330, 1334, 1350, 1358, 1359, 1395, 1400, 1422, 1448, 1455, 1457, 1475, 1481, 1483, 1496, 1523, 1579, 1607, 1621, 1631, 1637, 1660, 1671, 1728, 1739, 1743, 1748, 1796, 1886, 1898, 1925, 1953, 1955, 1967, 1975, 1986, 2002, 2142, 2150, 2198, 2251, 2254, 2343, 2380, 2425, 2446, 2657, 2685, 2758, 2908, 2925, 2963, 2969, 2980, 3043, 3087, 3156, 3163, 3231, 3298, 3382, 3399, 3428, 3462, 3544, 3666, 3939, 3977, 4127, 4196, 4199, 4231, 4251, 4255, 4405, 4448, 4479, 4518, 4582, 4627, 4717, 4733, 4751, 4803, 4966, 4994, 5079, 5231, 5405, 5468, 5517, 5526, 5563, 5565, 5571, 5784, 5880, 5916, 5925, 5962, 6008, 6123, 6167, 6422, 6479, 6840, 7522, 7548, 7555, 7724, 7755, 7820]


    for i2, line_data2 in enumerate(out_array_):
        for j2, col_data2 in enumerate(line_data2):

            if i2 not in filter_index_l2:
                ws.write(i2, j2, col_data2)  # 3个参数分别为行号，列号，和内容

    wb_.save('./write_test2.xls')


# write_xls(out_array)  # 写入根据人次 从大到小的信息
write_xls2(out_array)  # 比较原始优化的医院模板，寻找未匹配的医院模板








