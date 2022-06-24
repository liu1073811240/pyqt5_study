# -- coding: utf-8 --
# @Time : 2022/6/24 11:33
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : loadui.py
# @Software: PyCharm

from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("UI的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        from PyQt5.uic import loadUi
        loadUi('login.ui', self)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    def click():
        print("xxx")
        account = window.lineEdit.text()
        pwd = window.lineEdit_2.text()
        print(account)
        print(pwd)

    window.pushButton.clicked.connect(click)

    # print(dir(window))
    sys.exit(app.exec_())
