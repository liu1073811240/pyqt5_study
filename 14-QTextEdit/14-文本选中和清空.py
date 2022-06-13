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

    def ui3(self):  # 文本选中和清空
        tc = self.te.textCursor()
        # tc.setPosition(6)
        # tc.setPosition(6, QTextCursor.KeepAnchor)  # 保持锚点不变
        # tc.movePosition(QTextCursor.StartOfLine, QTextCursor.MoveAnchor, 1)  # 移动光标在指定位置
        # tc.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor, 1)
        # tc.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor, 1)
        # tc.select(QTextCursor.BlockUnderCursor)  # 选中某一个段落
        tc.select(QTextCursor.WordUnderCursor)  # 选中一个光标

        self.te.setTextCursor(tc)
        self.te.setFocus()

        return None


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())