# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\Front\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setEnabled(True)
        self.title_label.setGeometry(QtCore.QRect(220, 40, 441, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(83, 92, 381, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.user_label = QtWidgets.QLabel(self.widget)
        self.user_label.setObjectName("user_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.user_label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_lineEdit)
        self.pwd_label = QtWidgets.QLabel(self.widget)
        self.pwd_label.setObjectName("pwd_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pwd_label)
        self.pwd_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwd_lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_Button.setFont(font)
        self.login_Button.setObjectName("login_Button")
        self.horizontalLayout.addWidget(self.login_Button)
        self.cancel_Button = QtWidgets.QPushButton(self.widget)
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout.addWidget(self.cancel_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.user_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.user_textBrowser.setObjectName("user_textBrowser")
        self.gridLayout.addWidget(self.user_textBrowser, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "用户登录"))
        self.title_label.setText(_translate("mainWindow", "光电数据分析工具"))
        self.user_label.setText(_translate("mainWindow", "用户名"))
        self.pwd_label.setText(_translate("mainWindow", "密码"))
        self.login_Button.setText(_translate("mainWindow", "登录"))
        self.cancel_Button.setText(_translate("mainWindow", "退出"))
