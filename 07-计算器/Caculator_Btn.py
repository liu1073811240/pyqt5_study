# -- coding: utf-8 --
# @Time : 2022/8/5 16:39
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : Caculator_Btn.py
# @Software: PyCharm

from PyQt5.Qt import *


class CalculatorBtn(QPushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(CalculatorBtn, self).__init__(parent, *args, **kwargs)

        self.setStyleSheet("""
            background-color: red;
        
        """)