import sys
from PyQt5.Qt import *


class App(QApplication):
    def notify(self, receiver, evt):  # 重写notify

        # 如果接受对象是按钮控件，并且事件为鼠标点击按钮事件
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver, evt)

        return super().notify(receiver, evt)  # 信号分发，触发槽函数

class Btn(QPushButton):
    def event(self, evt):
        # print("按钮被点击了。。。")
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)  # 信号分发，触发槽函数

    def mousePressEvent(self, *args, **kwargs) -> None:
        print("鼠标被按下了。。。")
        return super().mousePressEvent(*args, **kwargs)  # 信号分发，触发槽函数


app = App(sys.argv)

window = QWidget()

btn = Btn(window)  # 将按钮控件放在窗口内部
btn.setText("按钮")
btn.move(100, 100)


def cao():
    print("按钮被点击了！")


btn.pressed.connect(cao)

window.show()

sys.exit(app.exec_())


