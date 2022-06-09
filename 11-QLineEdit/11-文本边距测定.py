# -- coding: utf-8 --
# @Time : 2022/6/8 10:02
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 10-光标位置控制.py
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
window.setWindowTitle("光标位置控制功能")
window.resize(500, 500)

le = QLineEdit(window)
le.move(100, 100)
le.resize(300, 300)
# le.setContentsMargins(100, 0, 0, 0)  # 设置内容外边距
le.setStyleSheet("background-color: cyan")
le.setTextMargins(0, 0, 50, 50)  # 设置文本外边距
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)


btn = QPushButton(window)
btn.setText("按钮")
btn.move(50, 50)

def cursor_move():
    # le.cursorBackward(False, steps=2)  # 光标向左移动steps数
    # le.cursorBackward(True, steps=2)  # 光标向左移动steps数,并选中相应文本
    # le.cursorForward(True, steps=2)  # 光标向右移动steps数,并选中相应文本
    # le.cursorWordBackward(True)  # 向前选中单词
    # le.cursorWordForward(True)  # 向后选中单词
    # le.home(True)  # 是否全部选中
    # le.end(False)  # 光标移到尾部

    # le.setCursorPosition(len(le.text()) / 2)  # 光标位置移动
    # le.setCursorPosition(1.5)
    # print(le.cursorPosition())  # 获取光标的位置

    # print(le.cursorPositionAt(QPoint(55, 105)))  # 这个点在哪个光标位置上。
    le.setText("社会我顺哥"*10)
    le.home(False)  # 所有文本最左侧
    le.setFocus()


btn.clicked.connect(cursor_move)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


