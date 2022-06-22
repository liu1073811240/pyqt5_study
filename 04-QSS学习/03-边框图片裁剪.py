# -- coding: utf-8 --
# @Time : 2022/6/15 16:41
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-QSS样式声明.py
# @Software: PyCharm

from PyQt5.Qt import *
from PIL import Image

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("样式声明的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        label = QLabel("标签测试", self)
        label.resize(300, 300)
        label.move(0, 0)

        self.qss(label)

    def qss(self, label):  # 角度渐变
        label.setStyleSheet("""
            QLabel {
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:0 red, stop:0.5 green, stop:1 orange);
                
                border-image: url(222_.png) 9px round;
                border-width: 9px;
                
            }
        """)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())