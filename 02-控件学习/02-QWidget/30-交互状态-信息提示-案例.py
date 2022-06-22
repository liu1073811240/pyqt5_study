# -- coding: utf-8 --
# @Time : 2022/5/23 11:13
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 30-交互状态-信息提示.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# window = QWidget()
window = QMainWindow()

# 懒加载： 用到的时候，才会加载
window.statusBar()

# 2.2 设置控件
window.setWindowTitle("信息提示案例")
window.resize(500, 500)
window.setWindowFlags(Qt.WindowContextHelpButtonHint)  # 设置带有问号的。

# 当鼠标停留在窗口控件之后，在状态栏提示的一段文本
window.setStatusTip("这是窗口")
print(window.statusTip())

label = QLabel(window)
label.setText("社会我顺哥")
label.setStatusTip("这是标签")
label.setToolTip("这是一个提示标签")
print(label.toolTip())

label.setToolTipDuration(2000)  # 设置提示标签时长
print(label.toolTipDuration())

label.setWhatsThis("这是啥？这是标签")

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
