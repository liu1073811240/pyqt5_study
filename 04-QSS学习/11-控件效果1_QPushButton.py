# -- coding: utf-8 --
# @Time : 2022/6/21 14:26
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 11-控件效果1_QPushButton.py
# @Software: PyCharm
from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("控件效果的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        w = QPushButton("按钮", self)
        w.resize(200, 200)
        w.move(100, 100)


if __name__ == '__main__':

    import sys
    from tool import QSSTool

    app = QApplication(sys.argv)

    QSSTool.setQssToObj("demo.qss", app)

    window = Window()
    window.show()

    sys.exit(app.exec_())