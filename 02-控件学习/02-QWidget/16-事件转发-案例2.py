# -- coding: utf-8 --
# @Time : 2022/5/19 10:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 15-事件转发-案例1.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtCore, QtGui
from PyQt5.Qt import *
import sys


class Mylabel(QLabel):
    def enterEvent(self, a0: QtCore.QEvent) -> None:
        print("鼠标进入")
        self.setText("欢迎光临")

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        print("鼠标离开")
        self.setText("谢谢惠顾")

    def keyPressEvent(self, evt) -> None:
        # QKeyEvent
        print("xxx")
        # if evt.key() == Qt.Key_Tab:
        #     print("用户点击了tab键")

        # 修饰键 Ctrl 普通键位 s
        # 如果用户的修饰键等于控制键 而且用户普通键等于控制键
        # if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
        #     print("ctrl + s被按下了")

        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_S:
            print("ctrl + shift + s被按下了")



# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("鼠标操作的案例1")
window.resize(500, 500)

label = Mylabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color: cyan")
label.grabKeyboard()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


