# -- coding: utf-8 --
# @Time : 2022/5/23 9:43
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 27-交互状态-活跃窗口.py
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
window.setWindowTitle("[*]交互状态")
window.resize(500, 500)

w2 = QWidget()
w2.show()

# 2.3 展示控件
window.show()

w2.raise_()

print(w2.isActiveWindow())
print(window.isActiveWindow())

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
