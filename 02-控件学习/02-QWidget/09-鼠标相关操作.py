
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
window.setWindowTitle("鼠标操作")
window.resize(500, 500)

# window.setCursor(Qt.BusyCursor)  # 鼠标繁忙状态
# window.setCursor(Qt.ForbiddenCursor)  # 鼠标禁止操作

label = QLabel(window)
label.setText("社会顺哥")
label.resize(100, 100)
label.setStyleSheet("background-color: cyan")

label.setCursor(Qt.ForbiddenCursor)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


