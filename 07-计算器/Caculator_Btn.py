# -- coding: utf-8 --
# @Time : 2022/8/5 16:39
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Caculator_Btn.py
# @Software: PyCharm

from PyQt5.Qt import *

# 对计算器按钮样式 进行设置

class CalculatorBtn(QPushButton):

    key_pressed = pyqtSignal(str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super(CalculatorBtn, self).__init__(parent, *args, **kwargs)
        # self.setAutoExclusive(True)  # 设置按钮样式 自动排斥。有可能被父控件覆盖

    def resizeEvent(self, *args, **kwargs):
        super(CalculatorBtn, self).resizeEvent(*args, **kwargs)
        # print(self.width() / 2)
        self.setStyleSheet("""
                    QPushButton[bg='gray'] {
                        color: white;
                        background-color: rgb(88, 88, 88);
                    }
                    QPushButton[bg='gray']:hover {
                        background-color: rgb(150, 150, 150);
                    }
                    QPushButton[bg='orange'], QPushButton[bg='equal'] {
                        color: white;
                        background-color: rgb(207, 138, 0);
                    }
                    QPushButton[bg='orange']:hover, QPushButton[bg='equal']:hover {
                        background-color: rgb(238, 159, 0);
                    }
                    QPushButton[bg='orange']:checked {
                        background-color: white;
                        color: rgb(207, 138, 0);
                    }
                    QPushButton[bg='lightgray'] {
                        color: black;
                        background-color: rgb(200, 200, 200);
                    }
                    QPushButton[bg='lightgray']:hover {
                        background-color: rgb(230, 230, 230);
                    }
                    QPushButton[bg] {
                        font--size: 20px;
                        border-radius: %dpx;
                    }
                    
                
                """ % (min(self.width(), self.height()) / 2))

    def mousePressEvent(self, *args, **kwargs) -> None:
        super().mousePressEvent(*args, **kwargs)
        self.key_pressed.emit(self.text(), self.property("role"))


