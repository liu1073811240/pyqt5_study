
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

# 按钮模拟点击
btn = QPushButton(window)
btn.setText("这是按钮")
btn.move(200, 200)
btn.pressed.connect(lambda: print("点击了这个按钮"))

# btn.click()
# btn.animateClick(2000)

btn2 = QPushButton(window)
btn2.setText("按钮2")


def test1():
    # btn.click()
    btn.animateClick(2000)  # 动画点击


btn2.pressed.connect(test1)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())

