# -- coding: utf-8 --
# @Time : 2022/6/27 14:58
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-decorator_signal.py
# @Software: PyCharm
from PyQt5 import QtCore
from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("装饰器连接信号与槽的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.setObjectName("btn")
        btn.resize(200, 200)
        btn.move(100, 100)

        btn2 = QPushButton("测试按钮2", self)
        btn2.setObjectName("btn2")
        btn2.resize(200, 200)
        btn2.move(100, 300)

        QMetaObject.connectSlotsByName(self)  # 将obj内部的子孙对象的信息，按照其objectName连接到相关的槽函数。
        # btn.clicked.connect(self.click)

    @pyqtSlot(bool)
    def on_btn_clicked(self, val):
        print("按钮被点击了！", val)

    # 相当于
    # self.btn.clicked[bool].connect(self.btn_clicked)
    # def btn_clicked(self):
    #     pass


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())