# -- coding: utf-8 --
# @Time : 2022/5/19 16:50
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 22-窗口相关操作2.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle("w1")

# print(window.windowState() == Qt.WindowNoState)  # 判断窗口为无状态

# window.setWindowState(Qt.WindowMinimized)  # 设置窗口为最小化状态
# window.setWindowState(Qt.WindowMaximized)  # 设置窗口为最大化状态
# window.setWindowState(Qt.WindowFullScreen)

w2 = QWidget()
w2.setWindowTitle("w2")

# 2.3 展示控件
window.show()
w2.show()

window.setWindowState(Qt.WindowActive)  # 让窗口活跃显示在最前面

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

