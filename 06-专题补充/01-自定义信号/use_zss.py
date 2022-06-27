# -- coding: utf-8 --
# @Time : 2022/6/27 15:49
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : use_zss.py
# @Software: PyCharm

from PyQt5.Qt import *
from test_decorator_ import Ui_Form

# qto


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("信号的学习")
        self.resize(500, 500)

        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("按钮被点击了！")

    @pyqtSlot()
    def on_pushButton_pressed(self):
        print("按钮被按下！")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())