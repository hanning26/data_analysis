# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\Front\data_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 13, 639, 470))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.factory_label = QtWidgets.QLabel(self.widget)
        self.factory_label.setObjectName("factory_label")
        self.verticalLayout.addWidget(self.factory_label)
        self.product_label = QtWidgets.QLabel(self.widget)
        self.product_label.setObjectName("product_label")
        self.verticalLayout.addWidget(self.product_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.factory_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.factory_lineEdit.setObjectName("factory_lineEdit")
        self.verticalLayout_2.addWidget(self.factory_lineEdit)
        self.product_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.product_lineEdit.setObjectName("product_lineEdit")
        self.verticalLayout_2.addWidget(self.product_lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chip_label = QtWidgets.QLabel(self.widget)
        self.chip_label.setObjectName("chip_label")
        self.verticalLayout_3.addWidget(self.chip_label)
        self.stamp_label = QtWidgets.QLabel(self.widget)
        self.stamp_label.setObjectName("stamp_label")
        self.verticalLayout_3.addWidget(self.stamp_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.chip_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.chip_lineEdit.setObjectName("chip_lineEdit")
        self.verticalLayout_4.addWidget(self.chip_lineEdit)
        self.stamp_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.stamp_lineEdit.setObjectName("stamp_lineEdit")
        self.verticalLayout_4.addWidget(self.stamp_lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_pushButton = QtWidgets.QPushButton(self.widget)
        self.search_pushButton.setObjectName("search_pushButton")
        self.horizontalLayout.addWidget(self.search_pushButton)
        self.analyse_pushButton = QtWidgets.QPushButton(self.widget)
        self.analyse_pushButton.setObjectName("analyse_pushButton")
        self.horizontalLayout.addWidget(self.analyse_pushButton)
        self.derive_pushButton = QtWidgets.QPushButton(self.widget)
        self.derive_pushButton.setObjectName("derive_pushButton")
        self.horizontalLayout.addWidget(self.derive_pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.show_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.show_textBrowser.setObjectName("show_textBrowser")
        self.gridLayout.addWidget(self.show_textBrowser, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.error_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.error_textBrowser.setLineWidth(1)
        self.error_textBrowser.setObjectName("error_textBrowser")
        self.gridLayout.addWidget(self.error_textBrowser, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.analyse_menu = QtWidgets.QMenu(self.menubar)
        self.analyse_menu.setObjectName("analyse_menu")
        self.chart_menu = QtWidgets.QMenu(self.analyse_menu)
        self.chart_menu.setObjectName("chart_menu")
        self.search_menu = QtWidgets.QMenu(self.menubar)
        self.search_menu.setObjectName("search_menu")
        self.tool_menu = QtWidgets.QMenu(self.menubar)
        self.tool_menu.setObjectName("tool_menu")
        self.auto_menu = QtWidgets.QMenu(self.menubar)
        self.auto_menu.setObjectName("auto_menu")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setObjectName("open_action")
        self.quit_action = QtWidgets.QAction(MainWindow)
        self.quit_action.setObjectName("quit_action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.mingjia_action = QtWidgets.QAction(MainWindow)
        self.mingjia_action.setObjectName("mingjia_action")
        self.shengpu_action = QtWidgets.QAction(MainWindow)
        self.shengpu_action.setObjectName("shengpu_action")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.normal_distribution_action = QtWidgets.QAction(MainWindow)
        self.normal_distribution_action.setObjectName("normal_distribution_action")
        self.scatter_action = QtWidgets.QAction(MainWindow)
        self.scatter_action.setObjectName("scatter_action")
        self.boxplot_action = QtWidgets.QAction(MainWindow)
        self.boxplot_action.setObjectName("boxplot_action")
        self.bar_action = QtWidgets.QAction(MainWindow)
        self.bar_action.setObjectName("bar_action")
        self.scatter_matrix_action = QtWidgets.QAction(MainWindow)
        self.scatter_matrix_action.setObjectName("scatter_matrix_action")
        self.func_action = QtWidgets.QAction(MainWindow)
        self.func_action.setObjectName("func_action")
        self.report_action = QtWidgets.QAction(MainWindow)
        self.report_action.setObjectName("report_action")
        self.start_action = QtWidgets.QAction(MainWindow)
        self.start_action.setObjectName("start_action")
        self.cut_action = QtWidgets.QAction(MainWindow)
        self.cut_action.setObjectName("cut_action")
        self.operation_guide_action = QtWidgets.QAction(MainWindow)
        self.operation_guide_action.setObjectName("operation_guide_action")
        self.lot_action = QtWidgets.QAction(MainWindow)
        self.lot_action.setObjectName("lot_action")
        self.data_consolidation_action = QtWidgets.QAction(MainWindow)
        self.data_consolidation_action.setObjectName("data_consolidation_action")
        self.data_format_conver_action = QtWidgets.QAction(MainWindow)
        self.data_format_conver_action.setObjectName("data_format_conver_action")
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.quit_action)
        self.chart_menu.addAction(self.normal_distribution_action)
        self.chart_menu.addAction(self.scatter_action)
        self.chart_menu.addAction(self.boxplot_action)
        self.chart_menu.addAction(self.bar_action)
        self.chart_menu.addAction(self.scatter_matrix_action)
        self.analyse_menu.addAction(self.chart_menu.menuAction())
        self.analyse_menu.addAction(self.func_action)
        self.analyse_menu.addAction(self.report_action)
        self.tool_menu.addAction(self.data_format_conver_action)
        self.tool_menu.addAction(self.data_consolidation_action)
        self.tool_menu.addAction(self.lot_action)
        self.auto_menu.addAction(self.start_action)
        self.auto_menu.addAction(self.cut_action)
        self.help_menu.addAction(self.operation_guide_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.auto_menu.menuAction())
        self.menubar.addAction(self.analyse_menu.menuAction())
        self.menubar.addAction(self.search_menu.menuAction())
        self.menubar.addAction(self.tool_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.factory_label.setText(_translate("MainWindow", "厂家"))
        self.product_label.setText(_translate("MainWindow", "产品名称"))
        self.chip_label.setText(_translate("MainWindow", "芯片名称"))
        self.stamp_label.setText(_translate("MainWindow", "印章/批号"))
        self.search_pushButton.setText(_translate("MainWindow", "搜索"))
        self.analyse_pushButton.setText(_translate("MainWindow", "分析"))
        self.derive_pushButton.setText(_translate("MainWindow", "导出"))
        self.file_menu.setTitle(_translate("MainWindow", "文件(F)"))
        self.analyse_menu.setTitle(_translate("MainWindow", "分析(F)"))
        self.chart_menu.setTitle(_translate("MainWindow", "图表"))
        self.search_menu.setTitle(_translate("MainWindow", "搜索(S)"))
        self.tool_menu.setTitle(_translate("MainWindow", "工具(T)"))
        self.auto_menu.setTitle(_translate("MainWindow", "自动化(A)"))
        self.help_menu.setTitle(_translate("MainWindow", "帮助(H)"))
        self.open_action.setText(_translate("MainWindow", "打开(O)"))
        self.quit_action.setText(_translate("MainWindow", "退出(Q)"))
        self.action_2.setText(_translate("MainWindow", "明镓"))
        self.action_3.setText(_translate("MainWindow", "升谱"))
        self.action_4.setText(_translate("MainWindow", "集佳"))
        self.action_5.setText(_translate("MainWindow", "卢米斯"))
        self.action_6.setText(_translate("MainWindow", "佑明"))
        self.mingjia_action.setText(_translate("MainWindow", "明镓"))
        self.shengpu_action.setText(_translate("MainWindow", "升谱"))
        self.action_10.setText(_translate("MainWindow", "集佳"))
        self.action_11.setText(_translate("MainWindow", "卢米斯"))
        self.action_12.setText(_translate("MainWindow", "佑明"))
        self.normal_distribution_action.setText(_translate("MainWindow", "正态分布图"))
        self.scatter_action.setText(_translate("MainWindow", "散点图"))
        self.boxplot_action.setText(_translate("MainWindow", "箱线图"))
        self.bar_action.setText(_translate("MainWindow", "柱状图"))
        self.scatter_matrix_action.setText(_translate("MainWindow", "散点图矩阵"))
        self.func_action.setText(_translate("MainWindow", "生成函数"))
        self.report_action.setText(_translate("MainWindow", "生成报告"))
        self.start_action.setText(_translate("MainWindow", "开始"))
        self.cut_action.setText(_translate("MainWindow", "终止"))
        self.operation_guide_action.setText(_translate("MainWindow", "操作指南"))
        self.lot_action.setText(_translate("MainWindow", "芯片批号-成品批号关系对应"))
        self.data_consolidation_action.setText(_translate("MainWindow", "数据合并(FT+RT)"))
        self.data_format_conver_action.setText(_translate("MainWindow", "数据格式转换"))
