# -- coding: utf-8 --
# @Time : 2022/5/31 16:42
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-文本的设置和获取.py
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
window.setWindowTitle("功能")
window.resize(500, 500)

le_a = QLineEdit(window)
le_a.move(100, 200)

le_b = QLineEdit(window)
le_b.move(100, 300)

copy_btn = QPushButton(window)  # 复制按钮
copy_btn.setText("复制")
copy_btn.move(100, 400)


def copy_cao():
    # 1. 获取文本框a、内容
    content = le_a.text()

    # 2. 把上面获取到的内容，设置到文本框B里面
    le_b.setText(content)

    # le_b.setText("")
    # le_b.insert(content)


copy_btn.clicked.connect(copy_cao)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

