from PyQt5 import QtGui
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("事件消息的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        pass

    def showEvent(self, QShowEvent):
        print("窗口被显示了出来")

    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")

    def moveEvent(self, QMoveEvent):
        print("窗口被移动了")

    def resizeEvent(self, QResizeEvent):
        print("窗口改变了尺寸大小")

    def enterEvent(self, QEvent):
        print("鼠标进来了")
        self.setStyleSheet("background-color: yellow")

    def leaveEvent(self, QEvent) -> None:
        print("鼠标移开了")
        self.setStyleSheet("background-color: green")

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标被按下")

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标被释放")

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标被双击了")

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标移动了")

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        print("键盘上某一个按键被按下了")

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        print("键盘上某一个按键被释放了")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
