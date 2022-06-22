import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

win1 = QWidget()
win1.setWindowTitle("红色")
win1.resize(500, 500)
win1.setStyleSheet("background-color: red;")
win1.show()

win2 = QWidget()
win2.setWindowTitle("绿色")
win2.setStyleSheet("background-color: green;")
# win2.setParent(win1)

win2.resize(1000, 100)
win2.show()

sys.exit(app.exec_())
