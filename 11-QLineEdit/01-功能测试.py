# -- coding: utf-8 --
# @Time : 2022/5/31 16:08
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-功能测试.py
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
window.setWindowTitle("QLineEdit功能测试")
window.resize(500, 500)

le = QLineEdit(window)
le.setText("sz")
# le.insert("18")

btn = QPushButton(window)
btn.setText("按钮")
btn.move(100, 100)
# btn.pressed.connect((lambda: le.insert("18")))  # 插入数字
# btn.pressed.connect(lambda: print(le.text()))  # 显示文本信息
btn.pressed.connect(lambda: print(le.displayText()))  # 显示文本信息


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

