# -- coding: utf-8 --
# @Time : 2022/5/30 15:19
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-菜单弹出模式2.py
# @Software: PyCharm

# qtt
# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("QToolButton的使用")
window.resize(500, 500)

tb = QToolButton(window)

tb.setText("工具")
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文本在图标下方
tb.setAutoRaise(True)  # 设置自动提升

# tb.setArrowType(Qt.NoArrow)  # 无箭头
# tb.setArrowType(Qt.UpArrow)  # 向上箭头
# tb.setArrowType(Qt.DownArrow)  # 向下箭头
# tb.setArrowType(Qt.LeftArrow)  # 向左箭头
tb.setArrowType(Qt.RightArrow)  # 向左箭头


menu = QMenu(window)
# menu.setTitle("菜单")
sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("123_.png"))

action1 = QAction(QIcon("123_.png"), "行为1", menu)
action1.setData([1, 2, 3])
action2 = QAction("行为2", menu)
action2.setData({"name": "sz"})
# action.triggered.connect(lambda: print("点击了行为菜单选项"))

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)

tb.clicked.connect(lambda: print("工具按钮被点击了！"))

tb.setMenu(menu)
tb.setPopupMode(QToolButton.MenuButtonPopup)  # 菜单按钮弹出模式
# tb.setPopupMode(QToolButton.InstantPopup)

def do_action(action):
    print("点击了行为", action.data())
tb.triggered.connect(do_action)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())
