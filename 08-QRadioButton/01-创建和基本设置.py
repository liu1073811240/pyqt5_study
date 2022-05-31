# -- coding: utf-8 --
# @Time : 2022/5/30 15:56
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-创建和基本设置.py
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

# rb_man = QRadioButton("男-&Male", window)
rb_man = QRadioButton("男", window)
rb_man.setShortcut("Alt+M")
rb_man.move(100, 100)
rb_man.setCheckable(True)

rb_woman = QRadioButton("女-&Female", window)
rb_woman.move(100, 150)
rb_woman.setIcon(QIcon("123_.png"))
rb_woman.setIconSize(QSize(60, 60))
rb_woman.toggled.connect(lambda isChecked: print(isChecked))

rb_woman.setAutoExclusive(False)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


