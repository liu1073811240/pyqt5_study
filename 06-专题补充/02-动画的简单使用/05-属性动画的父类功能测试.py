# -- coding: utf-8 --
# @Time : 2022/6/28 16:06
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-属性动画的父类功能测试.py
# @Software: PyCharm

from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("动画的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):

        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        btn.resize(200, 200)
        btn.setStyleSheet("background-color: cyan;")

        # 1. 创建一个动画对象，并且设置目标属性
        animation = QPropertyAnimation(btn, b"pos", self)  # 初始化类 属性动画
        # animation = QPropertyAnimation(self, b"windowOpacity", self)  # 初始化类 属性动画

        # 2. 设置属性值 开始 差值 结束
        animation.setStartValue(QPoint(0, 0))
        # animation.setKeyValueAt(0.5, 0.5)
        # animation.setKeyValueAt(1, 1)
        animation.setEndValue(QPoint(300, 300))

        # animation.setEndValue(0)

        # 3. 动画时长
        animation.setDuration(3000)  # 动画持续时间

        animation.setLoopCount(3)  # 设置循环次数

        # animation.setEasingCurve(QEasingCurve.InCurve)  # 动画按照 缓慢曲线规则走  -- 先快后慢
        # animation.setEasingCurve(QEasingCurve.OutCurve)  # 动画 先慢后快
        # animation.setEasingCurve(QEasingCurve.InBounce)
        animation.setEasingCurve(QEasingCurve.OutBounce)  # 设置曲线速度变化。

        animation.setDirection(QAbstractAnimation.Backward)  # 反方向运动

        # 4. 启动动画
        animation.start()
        print(animation.totalDuration(), animation.duration())  # 设置总时长、单次时长

        # btn.clicked.connect(lambda: print(animation.loopCount(), animation.currentLoop()))  # 设置循环次数、当前循环。
        # btn.clicked.connect(lambda: print(animation.currentTime(), animation.currentLoopTime()))  # 设置动画当前时间、当前循环时间。

        def animation_operation():
            if animation.state() == QAbstractAnimation.Running:
                animation.pause()  # 暂停
                # animation.stop()
            elif animation.state() == QAbstractAnimation.Paused:
                animation.resume()

            elif animation.state() == QAbstractAnimation.Stopped:
                animation.resume()

        btn.clicked.connect(animation_operation)  # 动画暂停与继续

        animation.currentLoopChanged.connect(lambda val: print("当前循环次数发生改变", val))
        animation.finished.connect(lambda: print("动画执行完毕"))

        animation.stateChanged.connect(lambda ns, os: print("状态发生改变", ns, os))


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
