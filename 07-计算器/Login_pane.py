# -- coding: utf-8 --
# @Time : 2022/7/18 16:09
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Login_pane.py
# @Software: PyCharm


from PyQt5.Qt import *
from resource.login import Ui_Form

# qto
class LoginPane(QWidget, Ui_Form):

    # exit_signal = pyqtSignal()  # 定义结束信号。
    # register_account_pwd_signal = pyqtSignal(str, str)  # 定义注册账户密码信号

    def __init__(self):
        super(LoginPane, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。
        self.setupUi(self)

        movie = QMovie(":/login/images/star.gif")  # 设置动画图片，展示动画效果。
        movie.setScaledSize(QSize(500, 232))
        self.login_top_bg_label.setMovie(movie)
        movie.start()




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = LoginPane()

    # window.exit_signal.connect(lambda: print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))

    window.show()

    sys.exit(app.exec_())
