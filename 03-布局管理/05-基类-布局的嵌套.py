from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("布局管理器的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # 创建4个子控件
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


        # 布局的嵌套
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")

        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")

        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")

        h_layout = QBoxLayout(QBoxLayout.LeftToRight)  # 横向排列, 从左到右排列
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)


        # 3. 把需要布局的子控件添加到布局管理器中
        layout.addWidget(label1)
        layout.addLayout(h_layout)

        layout.addWidget(label2)
        layout.addWidget(label3)

        layout.setEnabled(False)
        layout.setEnabled(True)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())