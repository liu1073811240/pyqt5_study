# -- coding: utf-8 --
# @Time : 2022/6/15 10:25
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : tool.py
# @Software: PyCharm


class QSSTool:
    @staticmethod
    def setQssToObj(file_path, obj):
        with open(file_path, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)

