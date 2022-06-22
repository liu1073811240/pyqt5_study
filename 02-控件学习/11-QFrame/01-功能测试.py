# -- coding: utf-8 --
# @Time : 2022/6/9 10:39
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-QTextEdit.py
# @Software: PyCharm


# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("QFrame的功能测试")
window.resize(500, 500)

frame = QFrame(window)
frame.resize(100, 100)
frame.move(100, 100)
frame.setStyleSheet("background-color: cyan")

# frame.setFrameShape(QFrame.Box)  # 设置黑边框
# frame.setFrameShape(QFrame.Panel)  # 凸起效果
# frame.setFrameShadow(QFrame.Raised)  # 设置外边框阴影
frame.setFrameStyle(QFrame.Box | QFrame.Raised)

frame.setLineWidth(10)
frame.setMidLineWidth(12)
print(frame.frameWidth())

frame.setFrameRect(QRect(20, 20, 60, 60))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

