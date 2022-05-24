
# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys
from PIL import Image


class MyWindow(QWidget):
    # QMouseEvent
    def mouseMoveEvent(self, me):
        print("鼠标移动了", me.globalPos())  # 鼠标的全局位置。
        print("鼠标移动了", me.localPos())  # 鼠标的局部位置


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWindow()

# 2.2 设置控件
window.setWindowTitle("鼠标操作")
window.resize(500, 500)
window.setMouseTracking(True)

print(window.hasMouseTracking())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


