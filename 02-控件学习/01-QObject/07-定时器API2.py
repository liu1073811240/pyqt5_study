
# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

'''
案例： 设置标签里面的数字时间变化

'''

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


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)

label = MyLabel(window)
label.setSec(5)  # 从5开始倒计时
label.startMyTimer(500)  # 间隔0.5s


# 2.3 展示控件
window.show()


# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


