# -- coding: utf-8 --
# @Time : 2022/6/9 15:41
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-占位文本测试.py
# @Software: PyCharm

from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QTextEdit功能的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        te = QTextEdit("xxx", self)
        self.te = te
        te.move(50, 50)
        te.resize(300, 300)
        te.setStyleSheet("background-color: cyan;")

        self.ui1()

    def ui1(self):  # 文本内容的设置
        # self.te.setPlainText("<h1>ooo</h1>")  # 设置普通文本
        # self.te.insertPlainText("<h1>ooo</h1>")  # 插入普通文本
        # print(self.te.toPlainText())  # 插入的普通文本

        # self.te.setHtml("<h1>ooo</h1>")  # 设置html字符串。富文本的操作。
        # self.te.insertHtml("<h6>社会我顺哥</h6>")
        # print(self.te.toHtml())

        self.te.setText("<h1>ooo</h1>")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())