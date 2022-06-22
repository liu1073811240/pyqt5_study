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

        test_btn = QPushButton(self)
        test_btn.move(10, 10)
        test_btn.setText("测试按钮")
        test_btn.pressed.connect(self.ui)

        te.textCursor().insertTable(5, 3)

    def ui(self):  # 换行模式设置
        # self.te.setLineWrapMode(QTextEdit.NoWrap)  # 不换行，后面会出现滚动条。

        # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)  # 设定固定像素宽度模式
        # self.te.setLineWrapColumnOrWidth(100)   # 设定固定像素宽度为100

        self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)  # 设定固定列宽模式
        self.te.setLineWrapColumnOrWidth(10)  # 设定固定列宽为10

        self.te.setWordWrapMode(QTextOption.WordWrap)  # 设置单词软换行模式，单词超过指定宽度就换行。


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())