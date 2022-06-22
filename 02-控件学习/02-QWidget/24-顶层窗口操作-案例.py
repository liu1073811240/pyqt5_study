# -- coding: utf-8 --
# @Time : 2022/5/19 18:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 24-顶层窗口操作-案例.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # 公共数据
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 40

        # 2.2 设置控件
        self.setWindowTitle("顶层窗口操作学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        # 添加三个子控件 - 窗口的右上角
        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)

        # close_btn_w = btn_w

        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)

        min_btn = QPushButton(self)
        self.min_btn = min_btn
        min_btn.setText("最小化")
        min_btn.resize(self.btn_w, self.btn_h)

        close_btn.pressed.connect(self.close)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText("恢复")

        max_btn.pressed.connect(max_normal)
        min_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        print("窗口大小发生了改变")

        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

    def mousePressEvent(self, evt):

        if evt.button() == Qt.LeftButton:  # 如果点击鼠标左键，才往下面执行。
            # QMouseEvent
            self.move_flag = True
            # print("鼠标按下")
            # 确定两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            # print(self.mouse_x, self.mouse_y)

            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        # print("鼠标移动")

        if self.move_flag:
            # 计算的是移动向量
            # print(evt.globalX(), evt.globalY())
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            # print(move_x, move_y)
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y

            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, evt):
        self.move_flag = False
        # print("鼠标释放")


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# window = QWidget(flags=Qt.FramelessWindowHint)
window = Window()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
