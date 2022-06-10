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

    def ui3(self):  # 光标插入列表
        tc = self.te.textCursor()
        # tl = tc.insertList(QTextListFormat.ListCircle)
        # tl = tc.insertList(QTextListFormat.ListDecimal)  # 十进制列表
        # tl = tc.createList(QTextListFormat.ListDecimal)  # 创建列表

        tlf = QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix("<<")
        tlf.setNumberSuffix("<<")
        tlf.setStyle(QTextListFormat.ListDecimal)

        tl = tc.createList(tlf)  # 创建列表
        print(tl)

        return None


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())