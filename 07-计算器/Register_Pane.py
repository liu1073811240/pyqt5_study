# -- coding: utf-8 --
# @Time : 2022/7/6 15:04
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Register_Pane.py
# @Software: PyCharm


from PyQt5.Qt import *
from resource.register import Ui_Form

# qto

class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。

        self.setupUi(self)


    def show_hide_menu(self, checked):
        print("显示和隐藏", checked)

    def about_lk(self):
        print("关于")

    def reset(self):
        print("重置")

    def exit_pane(self):
        print("退出界面")

    def check_register(self):
        print("注册")





if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
