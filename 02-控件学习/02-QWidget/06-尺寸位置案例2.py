'''

1. 通过给定的的个数,负责在一个窗口内创建相应个数的子控件
要求: 按照九宫格的布局进行摆放, 一行3列

'''

import sys
from PyQt5.Qt import *


app = QApplication(sys.argv)

window = QWidget()

# w = QWidget(window)
# w.resize(100, 100)
# w.setStyleSheet("background-color: red;")


window.show()

window.resize(500, 500)
window.move(300, 300)
# window.move(0, 0)

# 总控件个数
widget_count = 100

# 一行的列数
column_count = 3

# 计算一个控件的宽度
widget_width = window.width() / column_count

# 总共有多少行（编号 // 一行多少列 + 1）
row_count = (widget_count - 1) // column_count + 1

# 计算一个控件的高度
widget_height = window.height() / row_count

for i in range(0, widget_count):
    w = QWidget(window)
    w.resize(widget_width, widget_height)

    widget_x = (i % column_count) * widget_width  # 控件所在的列号 * 一个控件的宽度
    widget_y = (i // column_count) * widget_height  # 控件的Y所在的行号 * 一个控件的高度

    w.move(widget_x, widget_y)
    w.setStyleSheet("background-color: red; border: 1px solid yellow;")

    w.show()

sys.exit(app.exec_())


