# -- coding: utf-8 --
# @Time : 2022/5/23 14:04
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 31-焦点控制.py
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
window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(100, 100)

le3 = QLineEdit(window)
le3.move(150, 150)

# le2.setFocus()
# le2.setFocusPolicy(Qt.TabFocus)  # 只能通过tab键获取焦点。
# le2.setFocusPolicy(Qt.ClickFocus)  # 只能通过点击获取焦点
# le2.setFocusPolicy(Qt.StrongFocus)  # 通过tab键和点击都可以获取焦点
le2.setFocus()
le2.clearFocus()

# 2.3 展示控件
window.show()

# le1.clearFocus()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

