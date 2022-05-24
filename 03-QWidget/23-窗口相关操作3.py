# -- coding: utf-8 --
# @Time : 2022/5/19 17:19
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 23-窗口相关操作3.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle("w1")

# print(window.windowState() == Qt.WindowNoState)  # 判断窗口为无状态

# window.setWindowState(Qt.WindowMinimized)  # 设置窗口为最小化状态
# window.setWindowState(Qt.WindowMaximized)  # 设置窗口为最大化状态
# window.setWindowState(Qt.WindowFullScreen)


# 2.3 展示控件
window.show()
#
# window.showMaximized()
# window.showFullScreen()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
