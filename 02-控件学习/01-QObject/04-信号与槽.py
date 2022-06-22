import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

# 连接窗口标题变化的信号与槽
def cao(title):
    print("窗口标题变化了", title)
    # window.windowTitleChanged.disconnect()  # 防止死循环
    window.blockSignals(True)
    window.setWindowTitle("撩课-" + title)
    # window.windowTitleChanged.connect(cao)  # 让后面的操作建立连接。
    window.blockSignals(False)

window.windowTitleChanged.connect(cao)


window.setWindowTitle("Hello Sz")
window.setWindowTitle("Hello Sz2")
window.setWindowTitle("Hello Sz3")


window.show()


sys.exit(app.exec_())


