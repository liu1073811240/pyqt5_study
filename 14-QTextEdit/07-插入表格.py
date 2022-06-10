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
        test_btn.pressed.connect(self.ui2)

        # self.ui1()

    def ui1(self):  # 文本内容的设置

        self.te.append("<h3>ooo</h3>")

    def ui2(self):  # 按钮点击测试
        self.ui3()

    def ui3(self):  # 光标插入表格
        tc = self.te.textCursor()
        # tc.insertTable(5, 3)

        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        ttf.setCellPadding(6)
        ttf.setCellSpacing(13)

        # 设置列宽的约束
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50),
                                       QTextLength(QTextLength.PercentageLength, 40),
                                       QTextLength(QTextLength.PercentageLength, 10)))

        # QTextTable()
        # print(tc.insertTable(5, 3, ttf))
        table = tc.insertTable(5, 3, ttf)
        table.appendColumns(2)

        return None


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())