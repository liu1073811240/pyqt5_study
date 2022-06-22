# -- coding: utf-8 --
# @Time : 2022/5/25 16:24
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 09-设置点击的有效区域.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtCore, QtGui
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
window.resize(500, 500)


# 2.2 设置控件
class Btn(QPushButton):
    def hitButton(self, point):
        # print(point)  # 按钮的点
        # if point.x() > self.width() / 2:
        #     return True
        # else:
        #     return False
        # 通过给定的一个点坐标，计算与圆心的距离
        # 如果距离 < 半径 True
        # 否则返回 False

        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        # (x1 - x2)平方 + (y1 - y2)平方
        import math
        distance = math.sqrt(math.pow(hit_x - yuanxin_x, 2) + math.pow(hit_y - yuanxin_y, 2))
        print(distance)

        if distance < self.width() / 2:
            return True

        return False

    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 6))

        painter.drawEllipse(self.rect())


btn = Btn(window)
btn.move(100, 100)
btn.setText("点击")
btn.resize(200, 200)
# btn.setCheckable(True)
# btn.pressed.connect(lambda: print("按钮被按下了！"))
# btn.released.connect(lambda: print("按钮鼠标被释放！"))

# btn.clicked.connect(lambda value: print("按钮被点击！", value))

btn.toggled.connect(lambda value: print("按钮选中状态发生了改变", value))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


