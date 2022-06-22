from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QGridLayout的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()  # 网格布局

        self.setLayout(gl)

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        # 布局的嵌套
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")

        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")

        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 3, 3)  # 第一行第0列 到 占据3行、占据3列

        gl.addLayout(v_layout, 4, 0, 1, 4)

        # print(gl.getItemPosition(1))  # 获取第一行的所有控件的索引位置
        # print(gl.itemAtPosition(1, 1).widget().text())  # 获取第0行第一列的文本信息

        # gl.setColumnMinimumWidth(0, 100)  # 第0列，最小列宽为100
        # gl.setRowMinimumHeight(0, 100)  # 第0行，最小行高为100

        gl.setColumnStretch(0, 1)  # 设置第0列的控件拉伸系数为1
        gl.setColumnStretch(1, 2)

        gl.setRowStretch(4, 1)

        gl.setVerticalSpacing(60)

        gl.setHorizontalSpacing(60)

        print(gl.spacing())  # 水平间距、垂直间距默认为7
        print(gl.horizontalSpacing())  # 水平间距

        gl.setSpacing(60)

        gl.setOriginCorner(Qt.BottomRightCorner)  # 右下角为原点

        print(gl.rowCount())
        print(gl.columnCount())

        print(gl.cellRect(0, 1))
        print(gl.itemAtPosition(0, 1).widget().text())


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    gl = window.layout()

    print(gl.cellRect(0, 1))

    sys.exit(app.exec_())