# -- coding: utf-8 --
# @Time : 2022/5/24 16:36
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-文本设置.py
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
window.setWindowTitle("按钮的功能测试")
window.resize(500, 500)

btn = QPushButton(window)

# 图标设置
icon = QIcon("123_.png")
btn.setIcon(icon)
btn.setText("1")

size = QSize(50, 50)
btn.setIconSize(size)

# print(btn.icon())
# print(btn.iconSize())

# 快捷键的设定

def plus_one():
    print("加1")
    num = int(btn.text()) + 1

    btn.setText(str(num))

btn.pressed.connect(plus_one)

# btn.pressed.connect(lambda: print("按钮被点击了！"))
# btn.setShortcut("Alt+a")

# 自动重复
btn.setAutoRepeat(True)
btn.setAutoRepeatDelay(2000)  # 点击自动重复延迟时间
btn.setAutoRepeatInterval(1000)  # 点击自动重复间隔时间
# print(btn.autoRepeat())
# print(btn.autoRepeatInterval())
# print(btn.autoRepeatDelay())

push_button = QPushButton(window)
push_button.setText("这是QPushButton")
push_button.move(100, 100)

radio_button = QRadioButton(window)
radio_button.setText("这是一个radio")
radio_button.move(100, 150)

checkbox = QCheckBox(window)
checkbox.setText("这是checkbox")
checkbox.move(100, 200)

push_button.setStyleSheet("QPushButton:Pressed {background-color: red;}")

push_button.setCheckable(True)
print(push_button.isCheckable())  # 判断按钮是否可以被选中。
print(radio_button.isCheckable())
print(checkbox.isCheckable())

# 把三个按钮置为按下的状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)

push_button.setChecked(True)
radio_button.setChecked(True)
checkbox.setChecked(True)

print(push_button.isChecked())
print(radio_button.isChecked())
print(checkbox.isChecked())

def cao():
    push_button.toggle()
    radio_button.toggle()
    checkbox.toggle()

    # push_button.setChecked(not push_button.isChecked())


btn.pressed.connect(cao)

push_button.setEnabled(False)
radio_button.setEnabled(False)
checkbox.setEnabled(False)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
