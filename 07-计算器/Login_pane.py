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

    show_register_pane_signal = pyqtSignal()  # 展示注册面板信号。
    check_login_signal = pyqtSignal(str, str)  # 检查登录按钮信号。

    def __init__(self, parent=None, *args, **kwargs):
        super(LoginPane, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。
        self.setupUi(self)

        movie = QMovie(":/login/images/star.gif")  # 设置动画图片，展示动画效果。
        movie.setScaledSize(QSize(500, 232))
        self.login_top_bg_label.setMovie(movie)
        movie.start()

    def show_register_pane(self):  # 转到注册界面。
        self.show_register_pane_signal.emit()  # 发射要 展示注册面板信号。

    def open_qq_link(self):
        link = "https://user.qzone.qq.com/1073811240?source=namecardhoverqzone"
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        # print(account, pwd)
        if len(account) > 0 and len(pwd) > 0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.check_login_signal.emit(account, pwd)  # 发射信号出去。

    def auto_login(self, checked):
        print("自动登录", checked)
        if checked:
            self.remember_pwd_cb.setChecked(True)

    def remember_pwd(self, checked):
        print("记住密码", checked)
        if not checked:
            self.auto_login_cb.setChecked(False)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)  # 设置登录界面下半部分控件、做错误抖动特效。
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginPane()

    # window.exit_signal.connect(lambda: print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))

    window.show()

    sys.exit(app.exec_())
