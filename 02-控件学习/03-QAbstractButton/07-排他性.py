
# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
window.resize(500, 500)

# 2.2 设置控件

for i in range(0, 3):
    btn = QCheckBox(window)
    btn.setText("btn" + str(i))
    btn.move(50 * i, 50 * i)

    # btn.setAutoExclusive(False)  # 设置按钮排他性

    print(btn.autoExclusive())
    # print(btn.isCheckable())
    btn.setCheckable(True)

# btn = QPushButton(window)
# btn.setText("btn3")
# btn.move(250, 250)
# btn.setCheckable(True)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


