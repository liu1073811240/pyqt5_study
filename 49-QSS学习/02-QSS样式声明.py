# -- coding: utf-8 --
# @Time : 2022/6/15 16:41
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-QSS样式声明.py
# @Software: PyCharm

from PyQt5.Qt import *

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
        label.move(100, 100)

        # self.qss_border(label)
        # self.qss2(label)
        # self.qss3(label)
        self.qss4(label)

    def qss_border(self, label):
        label.setStyleSheet("""
            QLabel {
                background-color: cyan;
                border-width: 2em 16px;
                border-style: groove;
                border-bottom-width: 20px;
                border-color: red green orange blue;
                border-left-color: #00ff00;
            }
        
        """)
        # 上 右 下 左
        # 1em = 16px
        # groove 具有3D效果

    def qss2(self, label):  # 线性渐变
        label.setStyleSheet("""
            QLabel {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:0.4 gray stop:1 green);
                border-width: 2em 16px;
                border-style: groove;
                border-bottom-width: 20px;
                border-color: red green orange blue;
                border-left-color: #00ff00;
            }
        
        """)

    def qss3(self, label):  # 辐射渐变
        label.setStyleSheet("""
            QLabel {
                background-color: qradialgradient(cx:0.3, cy:0.7, radius:0.3, fx:0.7, fy:0.3, 
                stop:0 red, stop:0.5 green, stop:1 orange);
                
                border-width: 2em 16px;
                border-style: groove;
                border-bottom-width: 20px;
                border-color: red green orange blue;
                border-left-color: #00ff00;
            }
        """)

    def qss4(self, label):  # 角度渐变
        label.setStyleSheet("""
            QLabel {
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:0 red, stop:0.5 green, stop:1 orange);
                
                border-top-left-radius: 100px;
                border-width: 2em 16px;
                border-style: groove;
                border-bottom-width: 20px;
                border-color: red green orange blue;
                border-left-color: #00ff00;
            }
        """)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())