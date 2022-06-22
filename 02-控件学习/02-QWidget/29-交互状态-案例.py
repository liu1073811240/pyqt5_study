# -- coding: utf-8 --
# @Time : 2022/5/23 10:16
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 29-交互状态-案例.py
# @Software: PyCharm
from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("交互状态案例的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # 添加三个子控件
        label = QLabel(self)
        label.setText("标签")
        label.move(100, 50)
        label.hide()

        le = QLineEdit(self)
        # le.setText("文本框")
        le.move(100, 100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100, 150)
        btn.setEnabled(False)

        def text_cao(text):
            print("文本内容发生了改变", text)
            # if len(text) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)

            btn.setEnabled(len(text) > 0)

        le.textChanged.connect(text_cao)

        def check():
            # print("按钮被点击了")
            # 1. 获取文本框内容
            content = le.text()

            # 2. 判定是否是SZ
            # 3. 是-> 显示之前隐藏的标签，展示文本  否-> 展示标签、文本
            if content == 'SZ':
                label.setText("登录成功")
            else:
                label.setText("登录失败")

            label.show()
            label.adjustSize()

        btn.pressed.connect(check)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
