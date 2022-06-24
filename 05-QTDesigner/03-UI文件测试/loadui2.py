# -- coding: utf-8 --
# @Time : 2022/6/24 15:37
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : loadui2.py
# @Software: PyCharm

from PyQt5.Qt import *
from login import Ui_Form
# qto


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)

        self.setupUi(self)  # 直接类内部的实例方法。

    def setup_ui(self):
        pass

    def btn_click(self):
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    from login import Ui_Form

    # ui = Ui_Form()
    # ui.setupUi(window)

    sys.exit(app.exec_())
