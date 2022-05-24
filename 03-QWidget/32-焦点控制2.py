# -- coding: utf-8 --
# @Time : 2022/5/23 14:39
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 32-焦点控制2.py
# @Software: PyCharm
# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        # print(self.focusWidget())
        # self.focusNextChild()  # 点击 切换下一个焦点
        # self.focusPreviousChild()  # 点击 切换下一个焦点 （顺序相反）
        self.focusNextPrevChild(True)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(100, 100)

le3 = QLineEdit(window)
le3.move(150, 150)

QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

# 2.3 展示控件
window.show()

# print(le1)
# print(le2)
# print(le3)
# le2.setFocus()

# 获取当前窗口内部，所有子控件当中获取焦点的那个控件
# print(window.focusWidget())

# le1.clearFocus()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
