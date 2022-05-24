# -- coding: utf-8 --
# @Time : 2022/5/19 16:19
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 21-窗口相关操作.py
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

icon = QIcon("123_.png")
window.setWindowIcon(icon)  # 设置图标

# print(window.windowIcon())

window.setWindowTitle("社会")  # 设置窗口名称
# print(window.windowTitle())

window.setWindowOpacity(1.0)  # 设置窗口透明度
print(window.windowOpacity())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

