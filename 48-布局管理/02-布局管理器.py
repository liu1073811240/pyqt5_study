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
        label1 = QLabel("标签1", self)
        label1.setStyleSheet("background-color: cyan;")

        label2 = QLabel("标签2", self)
        label2.setStyleSheet("background-color: yellow;")

        label3 = QLabel("标签3", self)
        label3.setStyleSheet("background-color: red;")

        timer = QTimer(self)
        timer.timeout.connect(lambda: label1.setText(label1.text() + "itlike\n"))
        timer.start(1000)

        # 布局管理器
        v_layout = QVBoxLayout()
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        self.setLayout(v_layout)

        label2.hide()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())