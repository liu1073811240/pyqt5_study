from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        # self.QOject_test1()
        # self.QOjbect_test2()
        # self.QOjbect_test3()
        # self.QObject_test4()
        # self.QObject_test5()
        # self.QObject_test6()
        # self.QObject_test7()
        # self.QObject_test8()
        self.QObject_test9()

    def QOject_test1(self):  # QObject继承结构测试
        # QObject.__subclasses__()
        mros = QObject.mro()

        for mro in mros:
            print(mro)

    def QOjbect_test2(self):  # QObject对象名称和属性的操作
        # 测试API
        obj = QObject()
        obj.setObjectName("notice")
        print(obj.objectName())

        obj.setProperty("notice_level", "error")
        obj.setProperty("notice_level2", "warning")

        print(obj.property("notice_level"))

        print(obj.dynamicPropertyNames())

    def QOjbect_test3(self):  # 对象名称和属性的操作。
        with open("QObject.qss", 'r', encoding='utf-8') as f:
            qApp.setStyleSheet(f.read())  # 设置样式表属性

        # 案例演示
        label = QLabel(self)
        label.setObjectName("notice")
        label.setProperty("notice_level", "warning")
        label.setText("社会我顺哥")

        label2 = QLabel(self)
        label2.move(100, 100)
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "error")
        label2.setText("人狠话不多！")

        label3 = QLabel(self)
        label3.move(150, 150)
        label3.setText("人狠话不多！")

        btn = QPushButton(self)
        btn.setText("btn")
        btn.move(50, 50)


        # label.setStyleSheet("font-size: 20px; color: red;")

    def QObject_test4(self):  # 对象的父子关系操作。
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()

        print("obj0", obj0)
        print("obj1", obj1)
        print("obj2", obj2)
        print("obj3", obj3)
        print("obj4", obj4)
        print("obj5", obj5)

        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj2.setObjectName("2")
        # label = QLabel()
        # label.setParent(obj0)

        obj3.setParent(obj1)
        obj3.setObjectName("3")

        obj4.setParent(obj2)
        obj5.setParent(obj2)

        # print(obj4.parent())
        # print(obj1.parent())
        # print(obj0.children())

        # print(obj0.findChild(QObject, "3"))
        print(obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly))
        print(obj0.findChildren(QObject))

    def QObject_test5(self):  # 内存管理机制
        obj1 = QObject()
        self.obj1 = obj1

        obj2 = QObject()

        obj2.setParent(obj1)

        # 监听obj2对象被释放
        obj2.destroyed.connect(lambda :print("obj2对象被释放了"))

        del self.obj1

    def QObject_test6(self):  # 信号的操作
        self.obj = QObject()

        def destroy_cao(obj):
            print("对象被释放了！", obj)

        self.obj.destroyed.connect(destroy_cao)  # 如果这个对象被释放掉了，那么关联到的槽将被自动执行相应的操作。

        del self.obj

    def QObject_test7(self):  # 信号的操作2
        self.obj = QObject()

        def obj_name_cao(name):
            print("对象名称发生了改变", name)

        self.obj.objectNameChanged.connect(obj_name_cao)

        self.obj.setObjectName("xxx")

        self.obj.objectNameChanged.disconnect()

        self.obj.setObjectName("ooo")

    def QObject_test8(self):  # 信号的操作3
        self.obj = QObject()

        def obj_name_cao(name):
            print("对象名称发生了改变", name)

        def obj_name_cao2(name):
            print("对象名称发生了改变2", name)

        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.objectNameChanged.connect(obj_name_cao2)

        print(self.obj.receivers(self.obj.objectNameChanged))  # 信号连接槽的个数
        # self.obj.setObjectName("xxx")

        # self.obj.objectNameChanged.disconnect()
        print(self.obj.signalsBlocked(), '1')  # 信号是否发生了阻断。
        self.obj.blockSignals(True)  # 临时阻断了信号与槽的连接
        print(self.obj.signalsBlocked(), '2')

        self.obj.setObjectName("ooo")

        self.obj.blockSignals(False)
        print(self.obj.signalsBlocked(), '3')

        # self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.setObjectName("xxoo")

    def QObject_test9(self):  # 信号与槽的案例
        btn = QPushButton(self)
        btn.setText("点击我")


        def cao():
            print("点我干啥")

        btn.clicked.connect(cao)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())

