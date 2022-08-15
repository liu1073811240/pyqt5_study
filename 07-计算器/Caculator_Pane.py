# -- coding: utf-8 --
# @Time : 2022/8/3 18:12
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Caculator_Pane.py
# @Software: PyCharm

from PyQt5.Qt import *
from resource.caculator import Ui_Form


class Calculator(QObject):
    show_content = pyqtSignal(str)  # 展示内容的信息

    def __init__(self, parent):
        super(Calculator, self).__init__(parent)
        # self.setParent(parent)

        # 数字键位 num 运算符 operator
        self.key_models = []

    def calculate(self):
        if len(self.key_models) > 0 and self.key_models[-1]["role"] == "operator":
            self.key_models.pop(-1)
            print(self.key_models)

        expression = ""
        for model in self.key_models:
            expression += model["title"]
        print(expression)
        result = eval(expression)  # 计算“字符串”，
        print(result)

        return result

    def parse_key_model(self, key_model):
        # print(key_model)
        if key_model['role'] == 'clear':
            print("清空所有内容")
            self.key_models = []
            print(self.key_models)
            self.show_content.emit("0.0")
            return None

        if key_model['role'] == 'equal':
            print("计算所有内容")
            result = self.calculate()
            self.show_content.emit(str(result))
            return None

        # print(key_model)
        # num operator
        if len(self.key_models) == 0:
            if key_model["role"] == "num":
                if key_model["title"] == ".":  # # 判定如果是第一次添加小数点，那么就置为0.
                    key_model["title"] = "0."
                if key_model["title"] in ("%", "+/-"):   # 判断如果第一次是添加"%","+/-"的字符，那么就返回空
                    return None

                self.key_models.append(key_model)  # 判定如果是第一次添加数字，那么就加入列表
                self.show_content.emit(self.key_models[-1]["title"])
                print(self.key_models)
            return None
        # print(self.key_models)

        if key_model["title"] in ("%", "+/-"):  # 针对"%", "+/-"进行的处理
            if self.key_models[-1]["role"] != "num":
                return None
            else:
                if key_model["title"] == "%":
                    self.key_models[-1]["title"] = str(float(self.key_models[-1]["title"]) / 100)
                elif key_model["title"] == "+/-":
                    self.key_models[-1]["title"] = str(float(self.key_models[-1]["title"]) * -1)
                self.show_content.emit(self.key_models[-1]["title"])
            print(self.key_models)

            return None

        if key_model["role"] == self.key_models[-1]["role"]:
            if key_model["role"] == "num":

                if key_model["title"] == "." and self.key_models[-1]["title"].__contains__("."):
                    return None

                if self.key_models[-1]["title"] != "0":  # 如果前面一个和后面一个都为数字、且前面一个为字符串零的话，就做拼接
                    print('--111--')
                    self.key_models[-1]["title"] += key_model["title"]
                else:  # 如果前面一个和后面一个都为数字、且前面一个不为字符串零的话，就做替换
                    print('2222')
                    self.key_models[-1]["title"] = key_model["title"]
                self.show_content.emit(self.key_models[-1]["title"])
                print(self.key_models)

            # print(self.key_models)
            if key_model["role"] == "operator":
                self.key_models[-1]["title"] = key_model["title"]  # 如果前面一个和后面一个都为操作运算符的话，后面就替换前面
                self.show_content.emit(str(self.calculate()))
        else:
            print(key_model)
            if key_model["title"] in (".", "%", "+/-"):
                return None

            if key_model["role"] == "num":
                print('aaaa')
                print(key_model["title"])
                self.show_content.emit(key_model["title"])
            elif key_model["role"] == "operator":
                print('bbb')
                print(self.calculate())
                self.show_content.emit(str(self.calculate()))

            self.key_models.append(key_model)

        print(self.key_models)

# qto
class CaculatorPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(CaculatorPane, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景属性风格，让背景图片能够正常显示出来。
        self.setupUi(self)
        self.calculator = Calculator(self)
        self.calculator.show_content.connect(self.show_content)

    def show_content(self, content):
        self.lineEdit.setText(content)

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
