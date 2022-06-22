# -- coding: utf-8 --
# @Time : 2022/5/24 16:36
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-文本设置.py
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
window.setWindowTitle("按钮的功能测试")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("1")

def plus_one():
    print("加1")
    num = int(btn.text()) + 1

    btn.setText(str(num))

btn.pressed.connect(plus_one)

# 图标设置
icon = QIcon("123_.png")
btn.setIcon(icon)

size = QSize(50, 50)
btn.setIconSize(size)

print(btn.icon())
print(btn.iconSize())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


