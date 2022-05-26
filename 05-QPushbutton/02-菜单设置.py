# -- coding: utf-8 --
# @Time : 2022/5/26 14:30
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-构造函数.py
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
window.setWindowTitle("按钮的功能")
window.resize(500, 500)

btn = QPushButton(QIcon("123_.png"), '菜单', window)
# btn.setParent(window)
# btn.setText('xxx')
# btn.setIcon(QIcon("123_.png"))

# 菜单的设置
menu = QMenu()

# 子菜单  最近打开
open_recent_menu = QMenu()
open_recent_menu.setTitle("最近打开")

# 行为动作 新建 打开 分割线 退出
# new_action = QAction()
# new_action.setText("新建")
# new_action.setIcon(QIcon("123_.png"))
new_action = QAction(QIcon("123_.png"), "新建", menu)
new_action.triggered.connect(lambda: print("新建文件"))  # 新动作被点击触发 槽函数

open_action = QAction(QIcon("123_.png"), "打开文件", menu)
open_action.triggered.connect(lambda: print("打开文件"))  # 新动作被点击触发 槽函数

exit_action = QAction(QIcon("123_.png"), "退出", menu)
exit_action.triggered.connect(lambda: print("退出程序"))  # 新动作被点击触发 槽函数


menu.addAction(new_action)
menu.addAction(open_action)
menu.addSeparator()  # 分割位置
menu.addAction(exit_action)

btn.setMenu(menu)

btn.show()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环。
sys.exit(app.exec_())


