# -- coding: utf-8 --
# @Time : 2022/6/27 10:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-自定义信号.py
# @Software: PyCharm

from PyQt5.Qt import *

# qto
class Btn(QPushButton):
    rightClicked = pyqtSignal([str], [int, str])

    def mousePressEvent(self, evt) -> None:
        super(Btn, self).mousePressEvent(evt)

        # print(evt.button())  # 查看信号
        if evt.button() == Qt.RightButton:
            print("应该发射右击信号")
            self.rightClicked[str].emit(self.text())
            self.rightClicked[int, str].emit(888, 'itlike')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("信号的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # btn = QPushButton("xx", self)
        btn = Btn("xx", self)

        # btn.clicked.connect(lambda: print("按钮被点击了！"))
        btn.rightClicked[int, str].connect(lambda content, c2: print("按钮的右键被点击了！", content, c2))

        btn.pressed.connect(lambda: print("按钮的键被按下了！"))


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
