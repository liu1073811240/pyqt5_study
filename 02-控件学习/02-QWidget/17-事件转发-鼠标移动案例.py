# -- coding: utf-8 --
# @Time : 2022/5/19 11:24
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 17-事件转发-鼠标移动案例.py
# @Software: PyCharm
from PyQt5 import QtGui
from PyQt5.Qt import *

# qto


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.move_flag = False

        self.setWindowTitle("窗口移动学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self, evt):

        if evt.button() == Qt.LeftButton:  # 如果点击鼠标左键，才往下面执行。
            # QMouseEvent
            self.move_flag = True
            print("鼠标按下")
            # 确定两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            print(self.mouse_x, self.mouse_y)

            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        print("鼠标移动")

        if self.move_flag:
            # 计算的是移动向量
            print(evt.globalX(), evt.globalY())
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            print(move_x, move_y)
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y

            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, evt):
        self.move_flag = False
        print("鼠标释放")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    window.setMouseTracking(True)

    sys.exit(app.exec_())