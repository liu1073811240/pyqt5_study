# -- coding: utf-8 --
# @Time : 2022/5/26 14:30
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-构造函数.py
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
window.setWindowTitle("按钮的功能")
window.resize(500, 500)

btn = QPushButton(QIcon("123_.png"), 'xxx', window)
# btn.setParent(window)
# btn.setText('xxx')
# btn.setIcon(QIcon("xxx.png"))

btn.show()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


