
# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)


window = QWidget()
window.move(100, 100)
window.resize(200, 200)

print(window.x())  # 100
print(window.width())  # 200
print(window.geometry())  # PyQt5.QtCore.QRect(100, 100, 200, 200)


# 2.3 展示控件
window.show()

print('-' * 20)
print(window.x())  # 100
print(window.width())  # 200
print(window.geometry())  # PyQt5.QtCore.QRect(101, 138, 200, 200)


# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


