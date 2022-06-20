# -- coding: utf-8 --
# @Time : 2022/6/20 10:02
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-背景属性-案例.py
# @Software: PyCharm


# from PIL import Image
#
# img = Image.open('333.png')
# img = img.resize((637, 330))
# img.save('333_.png')


from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("背景属性的学习")
        self.resize(800, 800)

        self.setup_ui()

    def setup_ui(self):
        for i in range(0, 13):
            btn = QPushButton(self)
            btn.resize(86, 108)
            btn.setStyleSheet("""
                QPushButton {
                    background-image: url(333_.png);
                    border: 20px double red;
                    background-origin: content;
                    background-clip: padding;
                    
                    padding-left: -100px;
                    padding-top: -136px;
                    
                }
            
            """)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

