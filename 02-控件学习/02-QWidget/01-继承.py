
# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

# print(QWidget.__bases__)
# print(QWidget.mro())
window.setObjectName("xxx")
print(window.objectName())

red = QWidget(window)
red.resize(100, 100)
red.setStyleSheet("background-color: red;")
red.move(300, 0)

green = QWidget(window)
green.resize(100, 100)
green.setStyleSheet("background-color: green;")
green.move(300, 50)

window.show()


# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


