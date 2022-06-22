# -- coding: utf-8 --
# @Time : 2022/6/21 16:17
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 17-控件效果7_QSlider.py
# @Software: PyCharm




from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("控件效果的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):

        w = QSlider(Qt.Horizontal, self)

        w.resize(200, 40)
        w.move(100, 100)


if __name__ == '__main__':

    import sys
    from tool import QSSTool

    app = QApplication(sys.argv)

    QSSTool.setQssToObj("demo2.qss", app)

    window = Window()
    window.show()

    sys.exit(app.exec_())
