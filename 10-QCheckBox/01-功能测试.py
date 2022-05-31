# -- coding: utf-8 --
# @Time : 2022/5/31 14:33
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
window.setWindowTitle("功能测试")
window.resize(500, 500)

print(QCheckBox.__bases__)
cb = QCheckBox("&Python", window)
cb.setIcon(QIcon("xxx.png"))
cb.setIconSize(QSize(60, 60))
cb.setTristate(True)  # 设置三态

# cb.setChecked(True)
# cb.setChecked(Qt.PartiallyChecked)  # 设置选中状态
# cb.setCheckState(Qt.Checked)

cb.stateChanged.connect(lambda state: print(state))  # 监听状态信号改变
# cb.toggled.connect(lambda isChecked: print(isChecked))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
