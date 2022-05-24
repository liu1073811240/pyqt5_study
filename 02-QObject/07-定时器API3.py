
'''
案例：
1. 创建一个窗口, 通过定时器不断增加该窗口的大小。
2. 每 100ms 宽高均增加1px。

'''

from PyQt5.Qt import *
import sys



class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, '1')


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 22px;")
        # self.timer_id = self.startTimer(1000)

    def setSec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self, ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, *args, **kwargs):
        # print("xx")
        # 1. 获取当前标签的内容
        current_sec = int(self.text())  # 获取当前时间，字符串-->整形
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)


class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):  # 触发计时事件
        print("xxx")
        current_w = self.width()
        current_h = self.height()
        self.resize(current_w + 10, current_h + 10)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWidget()

# 2.2 设置控件
window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)

window.startTimer(100)  # 开始计时，每过0.1s要做的事情


# label = MyLabel(window)
# label.setSec(5)  # 从5开始倒计时
# label.startMyTimer(500)  # 间隔0.5s


# 2.3 展示控件
window.show()


# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

