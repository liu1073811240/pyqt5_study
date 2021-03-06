

# 0. 导入需要的包和模块
from PyQt5.Qt import *  # 主要包含了我们常用的一些类，汇总到了一块
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
# print(app.arguments())
# print(qApp.arguments())

# 2. 控件的操作。
# 创建控件，设置控件（大小，位置，样式。。。）, 事件，信号的处理。

# 2.1 创建控件
# 当我们创建一个控件之后，如果说，这个空间没有父控件，则把它当做顶层控件（窗口）。
# 系统会自动的给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题、图标）
window = QWidget()
# window = QPushButton()
# window = QLabel()

# 2.2 设置控件
# window.setText("hello sz")
window.setWindowTitle("基本结构分析")
window.resize(400, 400)

# 控件也可以作为一个容器（承载其它的控件）
label = QLabel(window)
label.setText("xxx")
# label.setWindowTitle("xxxxxx")
label.move(100, 50)
# label.show()

# 2.3 展示控件
# 刚创建一个控件之后，这个控件没有什么父控件。默认情况下不会展示，只有手动的调用show()才可以。
# 如果说这个控件有父控件，那么一般情况下，父控件展示之后，子控件也会展示。
window.show()

# 3. 应用程序的执行，进入到消息循环。
# 让整个程序开始执行，并且进入到消息循环（无限循环）
# 监测整个程序所接受到的用户的交互信息
sys.exit(app.exec_())


# 当别人通过命令行启动程序的时候， 可以设定一种功能，接受命令行传递的参数，来执行不同的业务逻辑。
# args = sys.argv
# print(args)
#
# if args[1] == '1':
#     print('xxx')
# else:
#     print("ooo")
