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
        label = QSpinBox(self)  #
        # layout = QVBoxLayout(self)
        # layout.addWidget(label)

        label.resize(300, 300)
        label.move(0, 0)

        self.qss1(label)

    def qss1(self, label):
        label.setStyleSheet("""
            QSpinBox {
                font-size: 26px;
                color: orange;
                border: 10px double red;
                border-radius: 10px;
                background-color: lightgray;
            
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 50px;
                height: 50px;
            }
            QSpinBox::up-button {
                subcontrol-origin: padding;
                subcontrol-position:left center;
                image: url(up_.png)
            }
            QSpinBox::up-button:hover {
                bottom: 10px;
            }
            QSpinBox::down-button {
                subcontrol-origin: padding;
                subcontrol-position:right center;
                image: url(down_.png)
            }
            QSpinBox::down-button:hover {
                position: absolute;
                top: 100px;
            }
        
        """)



if __name__ == '__main__':
    import sys
    from PIL import Image

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
