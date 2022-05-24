'''
1.创建一个窗口,设置尺寸为500 x 500，位置为300,300

'''

import sys
from PyQt5.Qt import *


app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
# window.move(300, 300)
window.move(0, 0)

window.show()

sys.exit(app.exec_())


