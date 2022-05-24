from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("布局管理器的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # 创建3个子控件
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color: orange;")

        # 1. 创建一个布局管理器对象
        layout = QBoxLayout(QBoxLayout.BottomToTop)

        # 2. 直接把布局管理器对象设置成需要布局的父控件
        self.setLayout(layout)

        # 3. 把需要布局的子控件添加到布局管理器中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        layout.setSpacing(60)

        # print(layout.contentsMargins().left())  # 查看左边的外边距
        # print(layout.contentsMargins().top())  # 查看上边的外边距
        layout.setContentsMargins(20, 40, 60, 80)

        layout.replaceWidget(label2, label4)

        label2.destroyed.connect(lambda : print("标签2被释放"))

        label2.hide()
        label2.setParent(None)
        print(label2.parent())


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())