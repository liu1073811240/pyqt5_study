from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color: orange;")

        # 1. 创建布局管理器对象
        # layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout = QHBoxLayout()

        # 2. 把布局管理器对象设置成需要布局的父控件
        self.setLayout(layout)

        # 3. 添加需要布局的子控件到布局管理器中。
        layout.addWidget(label1)
        layout.addStretch()
        layout.addWidget(label2)
        layout.addStretch()
        layout.addWidget(label3)
        # layout.addWidget(label4)

        # layout.setStretchFactor(label2, 1)

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")

        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")

        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")

        # h_layout = QBoxLayout(QBoxLayout.TopToBottom)  # 纵向排列
        h_layout = QVBoxLayout()
        h_layout.setDirection(QBoxLayout.RightToLeft)

        h_layout.addWidget(label5)
        h_layout.addWidget(label6, 1)  # 添加了伸缩因子，控件大小会随着窗口的大小做相应变化。
        h_layout.addWidget(label7)

        layout.addLayout(h_layout, 1)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
