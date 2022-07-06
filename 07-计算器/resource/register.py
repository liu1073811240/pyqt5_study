# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("QWidget#Form {\n"
                           "    border-image: url(:/register/images/register_background.webp);\n"
                           "\n"
                           "}\n"
                           "\n"
                           "")
        self.main_menu_btn = QtWidgets.QPushButton(Form)
        self.main_menu_btn.setGeometry(QtCore.QRect(20, 10, 50, 50))
        self.main_menu_btn.setStyleSheet("QPushButton {\n"
                                         "    border-radius: 25px;\n"
                                         "    background-color: rgb(131, 154, 255);\n"
                                         "    border: 2px solid rgb(37, 85, 185);\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    border: 4px rgb(76, 93, 200)\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:checked {\n"
                                         "    \n"
                                         "    background-color: rgb(30, 79, 169);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.exit_menu_btn = QtWidgets.QPushButton(Form)
        self.exit_menu_btn.setGeometry(QtCore.QRect(20, 90, 50, 50))
        self.exit_menu_btn.setStyleSheet("QPushButton {\n"
                                         "    border-radius: 25px;\n"
                                         "    background-color: rgb(131, 154, 255);\n"
                                         "    border: 2px solid rgb(37, 85, 185);\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    border: 4px rgb(76, 93, 200)\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:checked {\n"
                                         "    \n"
                                         "    background-color: rgb(30, 79, 169);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.exit_menu_btn.setCheckable(False)
        self.exit_menu_btn.setObjectName("exit_menu_btn")
        self.reset_menu_btn = QtWidgets.QPushButton(Form)
        self.reset_menu_btn.setGeometry(QtCore.QRect(70, 60, 50, 50))
        self.reset_menu_btn.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 25px;\n"
                                          "    background-color: rgb(131, 154, 255);\n"
                                          "    border: 2px solid rgb(37, 85, 185);\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    border: 4px rgb(76, 93, 200)\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:checked {\n"
                                          "    \n"
                                          "    background-color: rgb(30, 79, 169);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.reset_menu_btn.setCheckable(False)
        self.reset_menu_btn.setObjectName("reset_menu_btn")
        self.about_menu_btn = QtWidgets.QPushButton(Form)
        self.about_menu_btn.setGeometry(QtCore.QRect(100, 10, 50, 50))
        self.about_menu_btn.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 25px;\n"
                                          "    background-color: rgb(131, 154, 255);\n"
                                          "    border: 2px solid rgb(37, 85, 185);\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    border: 4px rgb(76, 93, 200)\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:checked {\n"
                                          "    \n"
                                          "    background-color: rgb(30, 79, 169);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.about_menu_btn.setCheckable(False)
        self.about_menu_btn.setObjectName("about_menu_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 190, 291, 222))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color: rgb(235, 231, 255);\n"
                                 "font: 12pt \"方正舒体\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setStyleSheet("background-color: transparent;\n"
                                    "color: rgb(203, 207, 197);\n"
                                    "border: none;\n"
                                    "border-bottom: 1px solid lightgray;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(235, 231, 255);\n"
                                   "font: 12pt \"方正舒体\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(203, 207, 197);\n"
                                      "border: none;\n"
                                      "border-bottom: 1px solid lightgray;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(235, 231, 255);\n"
                                   "font: 12pt \"方正舒体\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(203, 207, 197);\n"
                                      "border: none;\n"
                                      "border-bottom: 1px solid lightgray;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    background-color: rgb(120, 161, 255);\n"
                                      "    color: rgb(50, 103, 197);\n"
                                      "    border-radius: 10px;\n"
                                      "    \n"
                                      "    \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(174, 178, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    \n"
                                      "    background-color: rgb(93, 117, 255);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)

        self.retranslateUi(Form)
        self.main_menu_btn.clicked['bool'].connect(Form.show_hide_menu)
        self.about_menu_btn.clicked.connect(Form.about_lk)
        self.reset_menu_btn.clicked.connect(Form.reset)
        self.exit_menu_btn.clicked.connect(Form.exit_pane)
        self.pushButton.clicked.connect(Form.check_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menu_btn.setText(_translate("Form", "菜单"))
        self.exit_menu_btn.setText(_translate("Form", "退出"))
        self.reset_menu_btn.setText(_translate("Form", "重置"))
        self.about_menu_btn.setText(_translate("Form", "关于"))
        self.label.setText(_translate("Form", "账        号："))
        self.label_2.setText(_translate("Form", "密       码："))
        self.label_3.setText(_translate("Form", "确认密码："))
        self.pushButton.setText(_translate("Form", "注册"))


import images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
