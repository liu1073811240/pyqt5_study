# -- coding: utf-8 --
# @Time : 2022/5/19 15:08
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 19-父子关系-案例.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys

# class Label(QLabel):
#     def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
#         self.setStyleSheet("background-color: red;")

class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        local_x = evt.x()
        local_y = evt.y()

        sub_widget = self.childAt(local_x, local_y)  # 用户点击坐标位置的子控件
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color: red;")

        print("被点击了", local_x, local_y)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("父子关系案例")
window.resize(500, 500)

for i in range(1, 11):
    label = QLabel(window)
    label.setText("标签" + str(i))
    label.move(40*i, 40*i)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


