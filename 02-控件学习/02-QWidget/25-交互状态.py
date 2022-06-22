# -- coding: utf-8 --
# @Time : 2022/5/20 11:30
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 25-交互状态.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def paintEvent(self, evt) -> None:
        print("窗口被绘制了")

        return super().paintEvent(evt)


class Btn(QPushButton):
    def paintEvent(self, evt) -> None:
        print("按钮被绘制了")

        return super().paintEvent(evt)

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("交互状态")
window.resize(500, 500)

btn = Btn(window)
btn.setText("按钮")
btn.pressed.connect(lambda: print("按钮被点击了"))
# btn.pressed.connect(lambda: btn.setVisible(False))

# btn.setEnabled(False)  # 设置按钮是否可用
# btn.setVisible(False)
# print(btn.isEnabled())


# 2.3 展示控件
window.show()
# window.setVisible(True)
# window.setHidden(False)

# print(btn.isHidden())
# print(btn.isVisible())

btn.setVisible(False)
# 父控件如果显示的时候，子控件是否跟着被显示。
print(btn.isVisibleTo(window))  # 按钮相对于窗口是可见的。

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
