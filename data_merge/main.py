# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import sys
import merge_BP
import merge_TG
# import os
import datetime as dt
# import time
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressBar
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QWaitCondition, QMutex, QFileInfo
# 导入designer工具生成的login模块
from Ui_data_merge import Ui_MainWindow
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap

BP_directory = ''   # 保持标普数据合并文件夹地址
TG_directory = ''   # 保持台工数据合并文件夹地址

class init_Thread(QThread):  # 建立一个任务线程类
    signal = pyqtSignal(str)  # 设置触发信号传递的参数数据类型,这里是int
    
    def __init__(self, *args, **kwargs):
        super(init_Thread, self).__init__(*args, **kwargs)

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        self.signal.emit(str('0'))
        if BP_directory != '':
            merge_BP.path_init(BP_directory)
            self.signal.emit(str('25'))  # 任务线程发射信号用于与图形化界面进行交互
            if (merge_BP.init()):
                self.signal.emit(str('50'))  # 任务线程发射信号用于与图形化界面进行交互
        if TG_directory != '':
            merge_TG.path_init(TG_directory)
            self.signal.emit(str('75'))  # 任务线程发射信号用于与图形化界面进行交互
            if (merge_TG.init()):
                self.signal.emit(str('100'))  # 任务线程发射信号用于与图形化界面进行交互

class auto_Thread(QThread):  # 建立一个任务线程类
    signal = pyqtSignal(str)  # 设置触发信号传递的参数数据类型,这里是int
    
    def __init__(self, *args, **kwargs):
        super(auto_Thread, self).__init__(*args, **kwargs)
        self._isPause = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        self._isPause = True
 
    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        while 1:
            self.mutex.lock()
            if self._isPause:
                self.cond.wait(self.mutex)
            now_hour = dt.datetime.now().hour
            if (now_hour >= 21 and now_hour <= 24) or (now_hour >= 0 and now_hour <= 6):
                self.signal.emit(str('0'))
                if BP_directory != '':
                    merge_BP.path_init(BP_directory)
                    self.signal.emit(str('25'))
                    merge_BP.merge_main()
                    self.signal.emit(str('50'))
                if TG_directory != '':
                    merge_TG.path_init(TG_directory)
                    self.signal.emit(str('75'))
                    merge_TG.merge_main()
                    self.signal.emit(str('100'))
            else:
                self.signal.emit(str('-1'))
            self.msleep(60000)
            self.mutex.unlock()

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()  # 实例化一个QTimer实例
        self.initThraed = init_Thread()  # 实例化多线程类
        self.autoThraed = auto_Thread()  # 实例化多线程类
        self.setWindowTitle("Auto_Merge")
        root = QFileInfo(__file__).absolutePath()
        self.setWindowIcon(QIcon(root + '/images/auto-merge-cell.ico'))  # 设置图标
        # palette = QPalette()  # 设置背景
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("root + '/images/边框.png")))
        # self.setPalette(palette)

        self.flag = 0
        self.progressBar_1.setStyleSheet("QProgressBar { border: 2px solid grey; border-radius: 5px; color: rgb(20,20,20);  background-color: #FFFFFF; text-align: center;}QProgressBar::chunk {background-color: rgb(100,200,200); border-radius: 10px; margin: 0.1px;  width: 1px;}")
        self.news_textBrowser.setText("请选择标普/台工数据合并文件夹路径!\n")
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
        self.close_pushButton.clicked.connect(self.close)

    def BP_merge_folder(self):
        global BP_directory
        BP_directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")  # 起始路径
        self.news_textBrowser.append("标普数据合并文件夹路径为: " + BP_directory)

    def TG_merge_folder(self):
        global TG_directory
        self.news_textBrowser.setText("请选择台工数据合并文件夹路径!\n")
        TG_directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")  # 起始路径
        self.news_textBrowser.append("台工数据合并文件夹路径为: " + TG_directory)

    def init(self):
        self.progressBar_1.setFormat('初始化 %p%'.format(self.progressBar_1.value() - self.progressBar_1.minimum()))
        self.initThraed.signal.connect(self.init_progress_bar)
        self.initThraed.start()

    # init进度条
    def init_progress_bar(self, str):
        if ('0' in str):
            self.news_textBrowser.setText("开始初始化!\n")
            self.progressBar_1.setValue(0)
        if ('25' in str):
            self.news_textBrowser.append("BP初始化开始!\n")
            self.progressBar_1.setValue(25)
        if ('50' in str):
            self.news_textBrowser.append("BP初始化完成!\n")
            self.progressBar_1.setValue(50)
        if ('75' in str):
            self.news_textBrowser.append("TG初始化开始!\n")
            self.progressBar_1.setValue(75)
        if ('100' in str):
            self.news_textBrowser.append("TG初始化完成!\n")
            self.progressBar_1.setValue(100)

    def auto_merge(self):
        self.progressBar_1.reset()  # 进度条清空
        self.progressBar_1.setStyleSheet("QProgressBar { border: 2px solid grey; border-radius: 5px; color: rgb(20,20,20);  background-color: #FFFFFF; text-align: center;}QProgressBar::chunk {background-color: rgb(100,200,200); border-radius: 10px; margin: 0.1px;  width: 1px;}")
        self.progressBar_1.setFormat('合并中 %p%'.format(self.progressBar_1.value() - self.progressBar_1.minimum()))
        self.news_textBrowser.setText("合并开始!\n")
        self.autoThraed.signal.connect(self.auto_progress_bar)
        self.autoThraed.start()

    # auto进度条
    def auto_progress_bar(self, str):
        if ('0' in str):
            self.news_textBrowser.setText("合并开始!\n")
            self.progressBar_1.setValue(0)
        if ('25' in str):
            self.progressBar_1.setValue(25)
        if ('50' in str):
            self.progressBar_1.setValue(50)
        if ('75' in str):
            self.progressBar_1.setValue(75)
        if ('100' in str):
            self.news_textBrowser.append("合并完成!\n")
            self.progressBar_1.setValue(100)
        if ('-1' in str):
            self.news_textBrowser.setText("非程序运行时间段!\n")

    def stop(self):
        if (self.flag == 0):
            self.autoThraed.pause()
            self.news_textBrowser.setText("已暂停！\n")
            self.news_textBrowser.append("请再次点击暂停键开始！\n")
            self.flag = 1
        else:
            self.autoThraed.resume()
            self.flag = 0

if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
