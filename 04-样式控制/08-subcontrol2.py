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
        label = QCheckBox("复选框测试", self)
        label.resize(300, 300)
        label.move(0, 0)

        self.qss3(label)

    def qss3(self, label):
        label.setStyleSheet("""
            QCheckBox {
                color: gray;
                border: 10px double rgb(76, 76, 76);
                padding: 5px;       
            }
            QCheckBox::indicator{
                subcontrol-origin: border;
                subcontrol-position: left center;
                background: white;
                border: 2px solid gray;
            }
            QCheckBox::indicator:checked{
                background: rgb(76, 76, 76)
            
            }
            
            
        """)

        # background-origin: content  参照内容矩形。


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())