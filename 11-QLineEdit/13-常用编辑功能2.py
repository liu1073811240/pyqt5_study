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

le = QLineEdit(window)  # 文本编辑框
le.move(100, 100)
le.resize(300, 300)
# le.setContentsMargins(100, 0, 0, 0)  # 设置内容外边距
le.setStyleSheet("background-color: cyan")
le.setTextMargins(0, 0, 50, 50)  # 设置文本外边距
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)
le.setDragEnabled(True)  # 设置拖拽可用

le2 = QLineEdit(window)
le2.resize(50, 50)
le2.move(200, 0)

btn = QPushButton(window)
btn.setText("按钮")
btn.move(50, 50)


def cursor_move():

    le.cursorBackward(True, 3)  # 光标回退3个并选中, 粘贴并选中

    # le.copy()
    le.cut()

    le.setCursorPosition(0)
    le.paste()

    le.setFocus()


btn.clicked.connect(cursor_move)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


