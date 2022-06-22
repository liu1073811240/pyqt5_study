# -- coding: utf-8 --
# @Time : 2022/5/24 15:50
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-子类化抽象类.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("子类化抽象")
window.resize(500, 500)


class Btn(QAbstractButton):
    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        print("绘制按钮")

        # 绘制按钮上要展示的一个界面内容
        # 1. 创建一位画家,以及画在什么地方
        painter = QPainter(self)

        # 2. 给画家一个笔

        # 2.1 创建一个笔
        pen = QPen(QColor(111, 200, 50), 5)

        # 2.2 设置这个笔
        painter.setPen(pen)

        painter.drawText(20, 20, self.text())
        painter.drawEllipse(0, 0, 100, 100)  # 内切椭圆


btn = Btn(window)
btn.setText("xxx")
btn.resize(100, 100)

btn.pressed.connect(lambda : print("点击了按钮！"))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

