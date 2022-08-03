# -- coding: utf-8 --
# @Time : 2022/8/3 18:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Caculator_Pane.py
# @Software: PyCharm

from PyQt5.Qt import *
from resource.caculator import Ui_Form


# qto
class CaculatorPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(CaculatorPane, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = CaculatorPane()

    # window.exit_signal.connect(lambda: print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))

    window.show()

    sys.exit(app.exec_())