# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import sys
import merge
import os
import datetime as dt
import time
import threading
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressBar
from PyQt5.QtCore import QTimer
# 导入designer工具生成的login模块
from Ui_data_merge import Ui_MainWindow

BP_directory = ''   # 保持标普数据合并文件夹地址
TG_directory = ''   # 保持台工数据合并文件夹地址

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()  # 实例化一个QTimer实例
        self.flag = 0
        self.progressBar_1.setStyleSheet("QProgressBar { border: 2px solid grey; border-radius: 5px; color: rgb(20,20,20);  background-color: #FFFFFF; text-align: center;}QProgressBar::chunk {background-color: rgb(100,200,200); border-radius: 10px; margin: 0.1px;  width: 1px;}")
        # 添加FT_folder按钮信号和槽
        self.BP_merge_folder_action.triggered.connect(self.BP_merge_folder)
        # 添加RT_folder按钮信号和槽
        self.TG_merge_folder_action.triggered.connect(self.TG_merge_folder)
        # 添加初始化按钮信号和槽。注意init函数不加小括号()
        self.init_pushButton.clicked.connect(self.init)
        # 添加合并按钮信号和槽。注意merge函数不加小括号()
        self.merge_pushButton.clicked.connect(self.auto_merge)
        # 添加暂停按钮信号与槽。
        self.stop_pushButton.clicked.connect(self.stop)
        # 添加退出按钮信号和槽。调用close函数
        # 添加暂停按钮信号与槽。
        self.stop_pushButton.clicked.connect(self.stop)
        # 添加退出按钮信号和槽。调用close函数
        self.close_pushButton.clicked.connect(self.close)

    def on(self):
        self.flag = 1
        while True:
            if self.flag == 1:
                pass   
            else:
                break

    def BP_merge_folder(self):
        global BP_directory
        self.news_textBrowser.setText("请选择标普数据合并文件夹路径!\n")
        BP_directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")  # 起始路径
        self.news_textBrowser.append("标普数据合并文件夹路径为: " + BP_directory)

    def TG_merge_folder(self):
        global TG_directory
        self.news_textBrowser.setText("请选择台工数据合并文件夹路径!\n")
        TG_directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")  # 起始路径
        self.news_textBrowser.append("台工数据合并文件夹路径为: " + TG_directory)

    def init(self):
        self.progressBar_1.setFormat('初始化 %p%'.format(self.progressBar_1.value() - self.progressBar_1.minimum()))
        self.news_textBrowser.setText("初始化开始!\n")
        self.timer.start(1000)  # 设置定时器的定时间隔时间，为1000ms，即1秒
        if BP_directory != '':
            merge.path_init(BP_directory)
            self.progressBar_1.setValue(25)
            if (merge.init()):
                self.progressBar_1.setValue(50)
                self.news_textBrowser.append("BP初始化完成!\n")
                self.timer.start(1000)  # 设置定时器的定时间隔时间，为1000ms，即1秒
        if TG_directory != '':
            merge.path_init(TG_directory)
            self.progressBar_1.setValue(75)
            if (merge.init()):
                self.progressBar_1.setValue(100)
                self.news_textBrowser.append("TG初始化完成!\n")
                self.timer.stop()

    def auto_merge(self):
        self.progressBar_1.reset()  # 进度条清空
        self.progressBar_1.setStyleSheet("QProgressBar { border: 2px solid grey; border-radius: 5px; color: rgb(20,20,20);  background-color: #FFFFFF; text-align: center;}QProgressBar::chunk {background-color: rgb(100,200,200); border-radius: 10px; margin: 0.1px;  width: 1px;}")
        self.progressBar_1.setFormat('合并 %p%'.format(self.progressBar_1.value() - self.progressBar_1.minimum()))
        self.news_textBrowser.setText("合并开始!\n")
        self.timer.start(2000)  # 设置定时器的定时间隔时间，为1000ms，即1秒
        now_hour = dt.datetime.now().hour
        if (now_hour >= 21 and now_hour <= 24) or (now_hour >= 0 and now_hour <= 6):
            self.news_textBrowser.append("程序运行中!\n")
            if BP_directory != '':
                merge.path_init(BP_directory)
                self.progressBar_1.setValue(25)
                merge.merge_main()
                self.progressBar_1.setValue(50)
            if TG_directory != '':
                merge.path_init(TG_directory)
                self.progressBar_1.setValue(75)
                merge.merge_main()
                self.progressBar_1.setValue(100)
                self.news_textBrowser.append("合并完成!\n")   
        else:
            self.news_textBrowser.setText("非程序运行时间段!\n")
            time.sleep(5)

    def stop(self):
        ~(self.flag)
        self.news_textBrowser.setText("已暂停！\n")
        self.news_textBrowser.setText("请按任意键开始！\n")

if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
