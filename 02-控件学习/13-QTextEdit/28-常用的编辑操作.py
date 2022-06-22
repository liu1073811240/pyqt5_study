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

    def ui(self):  # 字符格式
        # self.te.copy()
        # self.te.paste()

        # self.te.selectAll()
        # self.te.setFocus()

        # print(self.te.find('xx', QTextDocument.FindBackward | QTextDocument.FindCaseSensitively))  # 往前查找关键词,区分大小写
        print(self.te.find('xx', QTextDocument.FindBackward | QTextDocument.FindCaseSensitively | QTextDocument.FindWholeWords))
        self.te.setFocus()
        pass


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
