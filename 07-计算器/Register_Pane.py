# -- coding: utf-8 --
# @Time : 2022/7/6 15:04
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Register_Pane.py
# @Software: PyCharm


from PyQt5.Qt import *
from resource.register import Ui_Form

# qto

class RegisterPane(QWidget, Ui_Form):

    exit_signal = pyqtSignal()  # 定义结束信号。
    register_account_pwd_signal = pyqtSignal(str, str)  # 定义注册账户密码信号

    def __init__(self):
        super(RegisterPane, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。
        self.setupUi(self)

        self.animation_targets = [self.about_menu_btn, self.reset_menu_btn, self.exit_menu_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

    def show_hide_menu(self, checked):
        # print("显示和隐藏", checked)

        animation_group = QSequentialAnimationGroup(self)  # 序列动画组
        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)  # 动画设置目标对象
            animation.setPropertyName(b"pos")

            animation.setStartValue(self.main_menu_btn.pos())
            animation.setEndValue(self.animation_targets_pos[idx])
            # if not checked:
            #     animation.setStartValue(self.main_menu_btn.pos())
            #     animation.setEndValue(self.animation_targets_pos[idx])
            # else:
            #     animation.setEndValue(self.main_menu_btn.pos())
            #     animation.setStartValue(self.animation_targets_pos[idx])

            animation.setDuration(200)  # 设置动画时长
            animation.setEasingCurve(QEasingCurve.InOutBounce)  # 设置动画变化（曲线）

            animation_group.addAnimation(animation)  # 动画行为添加到动画组

        # if not checked:
        #     animation_group.setDirection(QAbstractAnimation.Forward)  # 控制动画方向
        # else:
        #     animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.setDirection(checked)  # 根据布尔值 来决定动画方向

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def about_lk(self):
        print("关于")
        QMessageBox.about(self, "撩课学院", "https://www.itlike.com")

    def reset(self):
        print("重置")
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()

    def exit_pane(self):
        # print("退出界面")
        self.exit_signal.emit()  # 发出信号

    def check_register(self):
        print("注册")
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        self.register_account_pwd_signal.emit(account_txt, password_txt)

    def enable_register_btn(self):
        print("判定")
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        cp_txt = self.confirm_pwd_le.text()

        if len(account_txt) > 0 and len(password_txt) > 0 and len(cp_txt) > 0 and password_txt == cp_txt:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = RegisterPane()
    window.exit_signal.connect(lambda: print("退出"))
    window.register_account_pwd_signal.connect(lambda a, p: print(a, p))

    window.show()

    sys.exit(app.exec_())
