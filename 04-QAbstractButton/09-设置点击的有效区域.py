# -- coding: utf-8 --
# @Time : 2022/5/25 16:24
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 09-设置点击的有效区域.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtCore
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




btn = Btn(window)
btn.move(100, 100)
btn.setText("点击")
btn.resize(200, 200)
btn.pressed.connect(lambda: print("按钮被点击了！"))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


