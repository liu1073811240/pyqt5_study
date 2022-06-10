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

    def ui1(self):  # 占位文本的提示
        self.te.setPlaceholderText("请输入你的个人简介")
        print(self.te.placeholderText())  # 查看占位文本


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())