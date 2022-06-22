from PyQt5.Qt import *

# qto
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        name_label = QLabel("姓名(&n)：")
        age_label = QLabel("年龄(&g)：")

        name_le = QLineEdit()
        age_sb = QSpinBox()

        # name_label.setBuddy(name_le)
        # age_label.setBuddy(age_sb)

        sex_label = QLabel("性别：")
        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")

        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn = QPushButton("提交")

        # 1.创建布局管理器
        layout = QFormLayout()

        # 2.把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        # 3.把需要布局的子控件交给布局管理器进行布局
        # layout.setWidget(0, QFormLayout.LabelRole, name_label)  # 标签
        # layout.setWidget(0, QFormLayout.FieldRole, name_le)  # 输入框

        layout.addRow(name_label)
        print(layout.getWidgetPosition(name_label))
        layout.setWidget(0, QFormLayout.LabelRole, name_le)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())