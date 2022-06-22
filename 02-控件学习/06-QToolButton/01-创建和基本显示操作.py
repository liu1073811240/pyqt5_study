# -- coding: utf-8 --
# @Time : 2022/5/27 16:37
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-创建和基本显示操作.py
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
window.setWindowTitle("QToolButton的使用")
window.resize(500, 500)

tb = QToolButton(window)  # 只显示图标、不显示文字
tb.setText("工具")
tb.setIcon(QIcon("123_.png"))
tb.setIconSize(QSize(60, 60))
tb.setToolTip("这是一个新建按钮")

# tb.setToolButtonStyle(Qt.ToolButtonIconOnly)  # 只显示图标
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)  # 只显示图标
# tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 显示文本在图标的旁边
tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 文本在图标下方


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
