# -- coding: utf-8 --
# @Time : 2022/7/20 15:19
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : main.py
# @Software: PyCharm

from Login_pane import LoginPane
from Register_Pane import RegisterPane

from PyQt5.Qt import *


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login_pane = LoginPane()

    register_pane = RegisterPane(login_pane)  # 将登录面板作为 父控件、 注册面板作为子控件。
    register_pane.move(0, login_pane.height())
    register_pane.show()

    def exit_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(), 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register_pane():
        print("展示注册界面")

        # 设置 转到 注册界面的动画
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(register_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    register_pane.exit_signal.connect(exit_register_pane)  # 发射信号： 注册页面退出 转为 登录页面
    register_pane.register_account_pwd_signal.connect(lambda account, pwd: print(account, pwd))

    login_pane.show_register_pane_signal.connect(show_register_pane)  # 发射信号： 登录页面 转为 注册页面

    login_pane.show()

    sys.exit(app.exec_())

