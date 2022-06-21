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
        label = QLabel("标签测试" * 3, self)  # QLabel/QPushButton/QTextEdit
        layout = QVBoxLayout(self)
        layout.addWidget(label)

        # label.resize(300, 300)
        # label.move(0, 0)

        # self.qss(label)
        # self.qss2(label)
        # self.qss3(label)
        self.qss4(label)

    def qss(self, label):  # 角度渐变
        label.setStyleSheet("""
            QLabel {
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:0 red, stop:0.5 green, stop:1 orange);

                border-image: url(222_.png) 9px round;
                border-width: 9px;
                margin: 20px 40px 80px 160px;
                margin-left: 20px;
            }
        """)

    def qss2(self, label):  # 角度渐变
        label.setStyleSheet("""
            QLabel {
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:0 red, stop:0.5 green, stop:1 orange);
                color: orange;
                border:10px solid red;
                padding: 20px;
                padding-top: 150px;
            }
        """)

    def qss3(self, label):
        label.setStyleSheet("""
            QTextEdit {
                background-color: rgb(100, 200, 100);
                background-image: url(111_.png);
                background-repeat: no-repeat;
                background-position: left top;
                background-origin: border;
                background-clip: content;
                background-attachment: fixed;

                color: red;
                border:20px double red;
                padding: 20px;
                margin: 20px;
                
                font-family: 隶书;
            }
        """)

        # background-origin: content  参照内容矩形。

        # background-attachment: 背景图是否根据滚动

    def qss4(self, label):
        label.setStyleSheet("""
            QLabel {
                background-color: red;
                font-family: 隶书;
                font-size: 30px;
                font-style: italic;
                font-weight: 900;
                color: orange;
                
                min-width: 200px;
                min-height: 200px;
                max-width: 600px;
                max-height: 600px;
            }
        """)

        # font-weight: bold;


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
