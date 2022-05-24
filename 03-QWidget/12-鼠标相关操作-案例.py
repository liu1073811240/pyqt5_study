import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("鼠标相关操作案例")
        self.resize(500, 500)
        self.move(200, 200)
        self.setMouseTracking(True)

        pixmap = QPixmap("123_.png").scaled(50, 50)
        cursor = QCursor(pixmap)
        self.setCursor(cursor)

        label = QLabel(self)
        self.label = label
        label.setText("社会我顺哥，人狠话不多")
        label.move(100, 100)
        label.setStyleSheet("background-color: cyan;")

    def mouseMoveEvent(self, mv):
        print("鼠标移动", mv.localPos())
        # label = self.findChild(QLabel)
        # label.move(300, 300)
        # QPoint
        self.label.move(mv.localPos().x(), mv.localPos().y())


app = QApplication(sys.argv)

window = Window()


window.show()

sys.exit(app.exec_())
