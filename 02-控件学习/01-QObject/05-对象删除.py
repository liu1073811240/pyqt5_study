from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # self.QObject_test1()
        # self.QObject_test2()
        self.QObject_test3()

    def QObject_test1(self):  # 类型判定
        obj = QObject()
        w = QWidget()

        btn = QPushButton()
        label = QLabel()

        objs = [obj, w, btn, label]
        for o in objs:
            # print(o.isWidgetType())
            # print(o.inherits("QWidget"))  # 继承自QWidget
            print(o.inherits("QPushButton"))

    def QObject_test2(self):

        label1 = QLabel(self)
        label1.setText("社会我顺哥")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("人狠话不多")
        label2.move(150, 150)

        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(200, 200)

        # for widget in self.findChildren(QLabel):
        for widget in self.children():
            # if widget.isWidgetType():
            #     print("是")
            if widget.inherits("QLabel"):
                widget.setStyleSheet("background-color: cyan;")

    def QObject_test3(self):  # 对象删除
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda : print("obj1被释放了"))
        obj2.destroyed.connect(lambda : print("obj2被释放了"))
        obj3.destroyed.connect(lambda : print("obj3被释放了"))

        # del obj2
        obj2.deleteLater()  # 与父对象解除关联
        print(obj1.children())

        # 才会释放相关的对象




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())