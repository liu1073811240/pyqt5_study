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
        test_btn.pressed.connect(self.ui3)

        te.textCursor().insertTable(5, 3)

    def ui3(self):  # 开始和结束编辑块
        tc = self.te.textCursor()

        tc.beginEditBlock()
        tc.insertText("123")
        tc.insertBlock()
        tc.insertText("456")
        tc.insertBlock()
        tc.endEditBlock()

        tc.insertText("789")
        tc.insertBlock()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())