# -- coding: utf-8 --
# @Time : 2022/6/7 11:16
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 06-验证器案例.py
# @Software: PyCharm
import typing

from PyQt5.Qt import *

class AgeValidator(QValidator):
    def validate(self, input_str, pos_int):
        print(input_str)  # 输入的字符串内容
        print(pos_int)  # 光标的位置

        # 结果字符串， 应该全部都是由一些数字组成。 return
        try:
            if 18 <= int(input_str) <= 180:
                return QValidator.Acceptable, input_str, pos_int
            elif 1 <= int(input_str) <= 17:
                return QValidator.Intermediate, input_str, pos_int  # 验证器中间值
            else:
                return QValidator.Invalid, input_str, pos_int
        except:
            if len(input_str) == 0:
                return QValidator.Intermediate, input_str, pos_int
            return QValidator.Invalid, input_str, pos_int

    def fixup(self, p_str):
        print('xxx', p_str)
        try:
            if int(p_str) < 18:
                return "18"
            return "180"
        except:
            return "18"

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("验证器的使用")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)

        # 18 - 180
        validator = AgeValidator()
        le.setValidator(validator)

        le2 = QLineEdit(self)
        le2.move(200, 200)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())