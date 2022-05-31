# -- coding: utf-8 --
# @Time : 2022/5/30 16:36
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-多组互斥问题.py
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
window.setWindowTitle("QRadioButton-基本功能测试")
window.resize(500, 500)

red = QWidget(window)
red.resize(200, 200)
red.setStyleSheet("background-color: red;")
red.move(50, 50)

green = QWidget(window)
green.resize(100, 100)
green.setStyleSheet("background-color: green;")
green.move(red.x() + red.width(), red.y() + red.height())

rb_man = QRadioButton("男", red)
rb_man.setShortcut("Alt+M")
rb_man.move(10, 10)
rb_man.setCheckable(True)

rb_woman = QRadioButton("女-&Female", red)
rb_woman.move(10, 50)
rb_woman.setIcon(QIcon("123_.png"))
rb_woman.setIconSize(QSize(60, 60))
rb_woman.toggled.connect(lambda isChecked: print(isChecked))

rb_woman.setAutoExclusive(False)

rb_yes = QRadioButton("yes", green)
rb_yes.move(10, 10)
rb_no = QRadioButton("no", green)
rb_no.move(10, 50)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

