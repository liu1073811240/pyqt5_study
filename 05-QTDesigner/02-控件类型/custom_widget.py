# -- coding: utf-8 --
# @Time : 2022/6/23 16:27
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : custom_widget.py
# @Software: PyCharm
# 2.2 设置控件

from PyQt5.Qt import *
import sys

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
            print("小于半径")
            return True

        return False

    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 6))

        painter.drawEllipse(self.rect())


