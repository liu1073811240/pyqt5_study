# -- coding: utf-8 --
# @Time : 2022/6/21 11:01
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 09-级联和冲突.py
# @Software: PyCharm

from PyQt5.Qt import *

class Btn(QPushButton):
    pass

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("级联和冲突的学习")
        self.resize(500, 500)

        # self.setup_ui()
        # self.setup_ui2()
        self.setup_ui3()

    def setup_ui(self):
        btn1 = QPushButton("b1", self)
        btn2 = QPushButton("b2", self)
        btn1.setObjectName("b1")
        btn2.setObjectName("b2")

        btn1.move(100, 100)
        btn2.move(200, 200)

        self.setStyleSheet("""
            QPushButton#b1 {
                color: orange;
            }
            QPushButton {
                color: red;
            }
            
        """)

    def setup_ui2(self):
        btn1 = QPushButton("b1", self)
        btn2 = QPushButton("b2", self)
        btn1.setObjectName("b1")
        btn2.setObjectName("b2")

        btn1.move(100, 100)
        btn2.move(200, 200)

        self.setStyleSheet("""
            QPushButton:enabled:hover {
                color: red;
            }
            QPushButton:enabled {
                color: gray;
            }
            
        """)

    def setup_ui3(self):
        btn1 = Btn("b1", self)
        btn2 = QPushButton("b2", self)

        btn1.move(100, 100)
        btn2.move(200, 200)

        self.setStyleSheet("""
            Btn {color: orange;}
            QAbstractButton {
                color: gray;
            }
            
            QPushButton {
                color: red;
            }
            
        """)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())