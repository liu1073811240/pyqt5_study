# -- coding: utf-8 --
# @Time : 2022/7/20 15:19
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : main.py
# @Software: PyCharm

from Login_pane import LoginPane
from Register_Pane import RegisterPane
from Caculator_Pane import CaculatorPane
from PyQt5.Qt import *


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login_pane = LoginPane()

    register_pane = RegisterPane(login_pane)  # 将登录面板作为 父控件、 注册面板作为子控件。
    register_pane.move(0, login_pane.height())
    register_pane.show()

    caculator_pane = CaculatorPane()

    # 槽函数
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
        # animation.setStartValue(register_pane.pos())
        animation.setStartValue(QPoint(0, login_pane.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def check_login(account, pwd):
        if account == '1073811240' and pwd == "123456":
            print("登录成功")

            caculator_pane.show()
            login_pane.hide()
        else:
            login_pane.show_error_animation()

    # 信号的连接
    register_pane.exit_signal.connect(exit_register_pane)  # 发射信号： 注册页面退出 转为 登录页面
    register_pane.register_account_pwd_signal.connect(lambda account, pwd: print(account, pwd))

    login_pane.show_register_pane_signal.connect(show_register_pane)  # 发射信号： 登录页面 转为 注册页面
    login_pane.check_login_signal.connect(check_login)  # 登录面板

    login_pane.show()

    sys.exit(app.exec_())


'''
打包计算器程序：
安装pyinstaller: pip install pyinstaller
查看pyinstaller版本： pyinstaller --version

重新把项目放在一个新的路径，然后打包。

打包命令
1. pyinstaller main.py  # 会看到很多依赖包，可以自己添加缺少的文件。
2. pyinstaller -F main.py  # 不会看到很多依赖包，只打包成一个exe文件
3. pyinstaller -F -w main.py  # 只使用窗口，不显示命令窗口
4. pyinstaller -F -c main.py  # 既使用窗口，也显示命令窗口。

'''