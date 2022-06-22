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

    def ui(self):  # 字体设置
        # QFontDialog.getFont()

        # self.te.setFontFamily("幼圆")
        # self.te.setFontWeight(QFont.Black)
        # self.te.setFontItalic(True)
        # self.te.setFontPointSize(30)
        # self.te.setFontUnderline(True)

        font = QFont()
        font.setStrikeOut(True)  # 设置删除线
        self.te.setCurrentFont(font)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())