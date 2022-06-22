from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # 1. 创建一个布局管理器对象
        s1 = QStackedLayout(self)

        # 2.  把布局对象设置给需要布局的父控件 父布局
        self.setLayout(s1)

        # 3. 通过布局对象，管理布局一些子控件
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color: cyan;")

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6, 1)
        v_layout.addWidget(label7)

        print(s1.addWidget(label1))
        print(s1.addWidget(label2))
        print(s1.addWidget(label3))

        # print(s1.currentIndex())
        print(s1.insertWidget(10, label4))
        # print(s1.currentIndex())

        print(s1.widget(3).text())

        s1.setStackingMode(QStackedLayout.StackAll)
        # label1.hide()
        label1.setFixedSize(100, 100)
        label2.setFixedSize(150, 150)

        s1.removeWidget(label1)

        # print(label2.isVisible())
        # label2.show()

        # s1.setCurrentIndex(1)
        # print(s1.count())
        # print(s1.currentIndex())
        # timer = QTimer(self)
        # timer.timeout.connect(lambda: s1.setCurrentIndex((s1.currentIndex() + 1) % s1.count()))
        # timer.start(1000)

        # s1.setCurrentWidget(label4)

        # s1.currentChanged.connect(lambda val: print(val))




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())