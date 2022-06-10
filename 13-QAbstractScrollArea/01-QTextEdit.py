# -- coding: utf-8 --
# @Time : 2022/6/9 14:42
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-QTextEdit.py
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
window.setWindowTitle("QTextEdit父类功能测试")
window.resize(500, 500)

te = QTextEdit("社会顺哥", window)

te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 设置垂直滚动条, 一直显示
# te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 设置垂直滚动条，不显示出来

te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 设置水平滚动条
# te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 设置水平滚动条

btn = QPushButton(window)
btn.setIcon(QIcon("xxx.png"))

btn.pressed.connect(lambda : print("xxx"))
te.setCornerWidget(btn)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


