# -- coding: utf-8 --
# @Time : 2022/7/1 14:35
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 06-annimation_group.py
# @Software: PyCharm

from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("动画组的学习")
        self.resize(800, 800)

        self.setup_ui()

    def setup_ui(self):
        red_btn = QPushButton("红色按钮", self)
        green_btn = QPushButton("绿色按钮", self)

        red_btn.resize(100, 100)
        green_btn.resize(100, 100)

        red_btn.move(0, 0)
        green_btn.move(150, 150)

        red_btn.setStyleSheet("""
            background-color: red;
        
        """)

        green_btn.setStyleSheet("""
            background-color: green;
            
        """)

        animation = QPropertyAnimation(green_btn, b"pos", self)

        animation.setKeyValueAt(0, QPoint(150, 150))
        animation.setKeyValueAt(0.25, QPoint(550, 150))
        animation.setKeyValueAt(0.5, QPoint(550, 550))
        animation.setKeyValueAt(0.75, QPoint(150, 550))
        animation.setKeyValueAt(1, QPoint(150, 150))

        animation.setDuration(5000)
        animation.setLoopCount(3)
        # animation.start()  # 非阻塞式动画

        animation2 = QPropertyAnimation(red_btn, b"pos", self)

        animation2.setKeyValueAt(0, QPoint(0, 0))
        animation2.setKeyValueAt(0.25, QPoint(0, 700))
        animation2.setKeyValueAt(0.5, QPoint(700, 700))
        animation2.setKeyValueAt(0.75, QPoint(700, 0))
        animation2.setKeyValueAt(1, QPoint(0, 0))

        animation2.setDuration(5000)
        animation2.setLoopCount(3)
        # animation2.start()

        # animation_group = QParallelAnimationGroup(self)  # 并行动画组
        animation_group = QSequentialAnimationGroup(self)  # 串行动画组

        animation_group.addAnimation(animation)

        # animation_group.addPause(5000)  # 第一种方法：串行动画组才能暂停
        pause_animation = QPauseAnimation()  # 第二种方法：串行动画组暂停
        pause_animation.setDuration(3000)
        animation_group.addAnimation(pause_animation)

        animation_group.addAnimation(animation2)
        animation_group.start()

        red_btn.clicked.connect(animation_group.pause)
        green_btn.clicked.connect(animation_group.resume)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())