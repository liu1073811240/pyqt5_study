
# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys
from PIL import Image

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("鼠标操作")
window.resize(500, 500)

pixmap = QPixmap("123_.png")  # 自定义鼠标图标
new_pixmap = pixmap.scaled(50, 50)

cursor = QCursor(new_pixmap, 0, 0)
window.setCursor(cursor)

current_cursor = window.cursor()
current_cursor.setPos(100, 100)
print(current_cursor.pos())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


