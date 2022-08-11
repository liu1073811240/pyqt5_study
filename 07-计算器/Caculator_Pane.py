# -- coding: utf-8 --
# @Time : 2022/8/3 18:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Caculator_Pane.py
# @Software: PyCharm

from PyQt5.Qt import *
from resource.caculator import Ui_Form


class Calculator(QObject):
    def __init__(self, parent):
        super(Calculator, self).__init__(parent)
        # self.setParent(parent)

        # 数字键位 num 运算符 operator
        self.key_models = []

    def parse_key_model(self, key_model):
        # print(key_model)
        if key_model['role'] == 'clear':
            print("清空所有内容")
            return None

        if key_model['role'] == 'caculate':
            print("计算所有内容")
            return None

        # print(key_model)
        # num operator
        if len(self.key_models) == 0:
            if key_model["role"] == "num":
                self.key_models.append(key_model)  # 判定如果是第一次添加数字，那么就加入列表
                print(self.key_models)
            return None
        # print(self.key_models)

        if key_model["role"] == self.key_models[-1]["role"]:
            if key_model["role"] == "num":
                if self.key_models[-1]["title"] != "0":  # 如果前面一个和后面一个都为数字、且前面一个为字符串零的话，就做拼接
                    print('--111--')
                    self.key_models[-1]["title"] += key_model["title"]
                else:  # 如果前面一个和后面一个都为数字、且前面一个不为字符串零的话，就做替换
                    print('2222')
                    self.key_models[-1]["title"] = key_model["title"]
                print(self.key_models)

            # print(self.key_models)
            if key_model["role"] == "operator":
                self.key_models[-1]["title"] = key_model["title"]  # 如果前面一个和后面一个都为操作运算符的话，后面就替换前面
        else:
            self.key_models.append(key_model)

        print(self.key_models)

# qto
class CaculatorPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(CaculatorPane, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。
        self.setupUi(self)
        self.calculator = Calculator(self)

    def get_key(self, title, role):
        # print(title, role)  # self.text(), self.property("role")
        self.calculator.parse_key_model({"title": title, "role": role})  # 解析计算机的 值 及其相关属性


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = CaculatorPane()

    # window.exit_signal.connect(lambda: print("退出"))
    # window.register_account_pwd_signal.connect(lambda a, p: print(a, p))

    window.show()

    sys.exit(app.exec_())
