# -- coding: utf-8 --
# @Time : 2022/5/19 15:46
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 20-层级关系调整.py
# @Software: PyCharm


# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Label(QLabel):
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.raise_()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("层级关系的使用")
window.resize(500, 500)

label1 = Label(window)
label1.setText("标签1")
label1.resize(200, 200)
label1.setStyleSheet("background-color: red;")


label2 = Label(window)
label2.setText("标签2")
label2.resize(200, 200)
label2.setStyleSheet("background-color: green;")
label2.move(100, 100)

# label2.lower()  # 控件下降
# label1.raise_()  # 控件提升
# label2.stackUnder(label1)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

