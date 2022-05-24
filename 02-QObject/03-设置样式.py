import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

win_root = QWidget()

label1 = QLabel()
label1.setText("label1")
label1.setParent(win_root)

label2 = QLabel()
label2.move(50, 50)
label2.setText("label2")
label2.setParent(win_root)

label3 = QLabel()
label3.move(80, 80)
label3.setText("label3")
label3.setParent(win_root)

btn = QPushButton(win_root)
btn.move(100, 100)
btn.setText("btn")

win_root.show()

for sub_widget in win_root.findChildren(QLabel):
    print(sub_widget)
    sub_widget.setStyleSheet("background-color: cyan;")


sys.exit(app.exec_())
