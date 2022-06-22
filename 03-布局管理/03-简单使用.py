from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("布局管理的学习")
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

        # 布局管理器
        v_layout = QHBoxLayout()
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        v_layout.setContentsMargins(20, 30, 40, 50)  # 设置外边距 、（左、上、右、下）
        v_layout.setSpacing(60)  # 设置控件之间的间距。

        self.setLayout(v_layout)

        self.setLayoutDirection(Qt.RightToLeft)  # 设置布局控件的方向。

        print(self.children())


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())