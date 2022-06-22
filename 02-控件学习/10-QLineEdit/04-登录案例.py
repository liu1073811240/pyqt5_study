# -- coding: utf-8 --
# @Time : 2022/6/6 10:32
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-登录案例.py
# @Software: PyCharm

from PyQt5.Qt import *

class AccountTool:
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3
    @staticmethod
    def check_login(account, pwd):
        # 把账号和密码发送给服务器，等待用户返回结果
        if account != "sz":
            return AccountTool.ACCOUNT_ERROR
        if pwd != "itlike":
            return AccountTool.PWD_ERROR

        return AccountTool.SUCCESS

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("登录案例")
        self.resize(500, 500)
        self.setMinimumSize(400, 400)

        self.setup_ui()

    def setup_ui(self):

        # 添加三个控件
        self.account_le = QLineEdit(self)
        self.pwd_le = QLineEdit(self)
        self.pwd_le.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton(self)
        self.login_btn.setText("登 录")

        # 占位文本的提示
        self.account_le.setPlaceholderText("请输入账户")
        self.pwd_le.setPlaceholderText("请输入密码")

        # 设置密码文本框、自动显示清空按钮
        self.pwd_le.setClearButtonEnabled(True)

        # 添加自定义行为操作（明文和密文的切换）

        action = QAction(self.pwd_le)
        action.setIcon(QIcon("close_eye.jpeg"))  # 默认为密文模式

        def change():
            print("改变明文和密文")
            if self.pwd_le.echoMode() == QLineEdit.Normal:  # 如果密码为可视化模式
                self.pwd_le.setEchoMode(QLineEdit.Password)  # 文本框设置成密码模式
                action.setIcon(QIcon("close_eye.jpeg"))
            else:
                self.pwd_le.setEchoMode(QLineEdit.Normal)  # 文本可以看到
                action.setIcon(QIcon("open_eye.jpeg"))

        action.triggered.connect(change)  # 点击动作（小眼睛）连接相关信息
        self.pwd_le.addAction(action, QLineEdit.TrailingPosition)  # 将图片放在尾部
        # self.pwd_le.addAction(action, QLineEdit.LeadingPosition)  # 将图片放在头部

        self.login_btn.clicked.connect(self.login_cao)

        # 设置自动补全
        completer = QCompleter(["sz", "shunzi", "wangzha"], self.account_le)
        self.account_le.setCompleter(completer)

    def login_cao(self):

        account = self.account_le.text()
        pwd = self.pwd_le.text()

        state = AccountTool.check_login(account, pwd)

        if state == AccountTool.ACCOUNT_ERROR:
            print("账户错误")
            self.account_le.setText("")
            self.pwd_le.setText("")
            self.account_le.setFocus()
            return None

        if state == AccountTool.PWD_ERROR:
            print("密码错误")
            self.pwd_le.setText("")  # 清空密码文本框
            self.pwd_le.setFocus()  # 设置焦点
            return None

        print("登录成功")

        # if account != "sz":
        #     print("账户错误")
        #     self.account_le.setText("")
        #     self.pwd_le.setText("")
        #     self.account_le.setFocus()
        #     return None
        #
        # if pwd != "itlike":
        #     print("密码错误")
        #     self.pwd_le.setText("")  # 清空密码文本框
        #     self.pwd_le.setFocus()  # 设置焦点
        #     return None
        #
        # print("登录成功")

        # if account == "sz":
        #     if pwd == "itlike":
        #         print("登录成功")
        #     else:
        #         print("密码错误")
        #         self.pwd_le.setText("")  # 清空密码文本框
        #         self.pwd_le.setFocus()  # 设置焦点
        # else:
        #     print("账户错误")
        #     self.account_le.setText("")
        #     self.pwd_le.setText("")
        #     self.account_le.setFocus()

    def resizeEvent(self, evt) -> None:  # 尺寸变形事件
        widget_w = 150
        widget_h = 40
        margin = 60

        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.login_btn.resize(widget_w, widget_h)

        x = (self.width() - widget_w) / 2  # 控件x轴位置

        self.account_le.move(x, self.height() / 4)
        self.pwd_le.move(x, self.account_le.y() + widget_h + margin)
        self.login_btn.move(x, self.pwd_le.y() + widget_h + margin)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())