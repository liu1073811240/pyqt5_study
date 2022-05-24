from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QSS学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        box1 = QWidget(self)
        box2 = QWidget(self)

        # box1.setStyleSheet("QPushButton {background-color: orange;}")
        # box2.setStyleSheet("background-color: cyan;")

        label1 = QLabel("标签1", box1)
        label1. move(50, 50)
        btn1 = QPushButton("按钮1", box1)
        btn1.move(150, 50)
        btn1.setStyleSheet("background-color: orange;")

        label2 = QLabel("标签2", box2)
        label2.move(50, 50)
        btn2 = QPushButton("按钮2", box2)
        btn2.move(150, 50)

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        v_layout.addWidget(box1)
        v_layout.addWidget(box2)

        # self.setStyleSheet("QPushButton {background-color: orange;}")

        self.other_btn = QPushButton("按钮3")
        self.other_btn.show()

        # self.setStyleSheet("QPushButton {background-color: orange;}")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    # app.setStyleSheet("QPushButton {background-color: orange;}")  # 设置全局按钮为橘黄色。

    sys.exit(app.exec_())