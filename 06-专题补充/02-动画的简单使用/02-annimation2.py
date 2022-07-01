# -- coding: utf-8 --
# @Time : 2022/6/28 10:04
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-annimation2.py
# @Software: PyCharm
from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("动画的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        btn.resize(200, 200)
        btn.setStyleSheet("background-color: cyan;")

        # 1. 创建一个动画对象，并且设置目标属性
        animation = QPropertyAnimation(btn, b"size", self)  # 初始化类 属性动画

        # 2. 设置属性值 开始 差值 结束
        animation.setStartValue(QSize(0, 0))
        animation.setEndValue(QSize(300, 300))

        # 3. 动画时长
        animation.setDuration(3000)  # 动画持续时间

        # 4. 启动动画
        animation.start()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())