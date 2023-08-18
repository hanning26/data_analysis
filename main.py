#明镓4343数据分析
from scipy import stats
import xlwings as xw
import datetime as dt
import pandas as pd
from pathlib import Path

paths = (r'C:\Users\hanning\Desktop\汽车级4343测试数据分析\测试数据-4343-300片').replace('\\','//')
data_conversion_paths = (r'C:\Users\hanning\Desktop\汽车级4343测试数据分析\测试数据转换').replace('\\','//')
data = pd.DataFrame()
fun_datas = pd.DataFrame()
csvdirs = []
csvFiles = []
dir_files_dic = {}
data_dic = {}   #保存dataframe数据到字典
data_columns = ['VF1','VF2','VF3','VF4','VF5','VFD','LOP1','WLP1','HW1','WLD1','TWLS','INTENS','IV3','WLP3','HW3','WLD3',
'IR','IR2','IR3','LOP3/LOP2','deltaWLD','DWD','deltaIV','deltaVF','CALC']
data_conversion_columns = ['VF1','VF2','Vf3','Vf4','Vf5','VFD','LOP1','WLP','HW','WLD','TWLS','Iv3','WLP3','HW3','Wd3','IR','Ir2',
'Ir3','LOP3/LOP2','deltaWLD','DWD','deltaIV','deltaVF','CALC']
drop_col = ['TEST','BIN','CONTA','CONTC','POLAR','DVF', 'VZ','LOP2','WLP2','HW2','WLD2','Ir4','Ir5','PosX','PosY']
#后续加入参数规范与测试数据对比功能
parm_columns = {'VF1':(2.8,3.3), 'VF2':(2.2,2.4), 'VF3':(2.6,2.8),'VFD':(0,0.05), 
'LOP1':(1040,1300), 'WLP1':(430,470),'HW1':(14,21), 'WLD1':(445,465),'WLP3':(430,470),
'HW3':(14, 21),'WLD3':(445, 465),'IR':(0, 0.05),'IR2':(0, 0.05),'IR3':(0, 0.05)}


# 文件存放地址
data_analysis_path = r'C:\Users\hanning\Desktop\汽车级4343测试数据分析\数据分析'
data_analysis_path = data_analysis_path.replace('\\','//') 

Fun_Data_path = data_analysis_path + '//Fun_Data//CP//'
Scatter_Plot_path = data_analysis_path + '//Scatter_Plot//CP//'
Scatter_Matrix_path = data_analysis_path + '//Scatter_Matrix//CP//'
Bar_Chart_path = data_analysis_path + '//Bar_Chart//CP//'
Normal_Distribution_path = data_analysis_path + '//Normal_Distribution//CP//'
Box_Drawings_path = data_analysis_path + '//Box_Drawings//CP//'

# --------------------------Main Program-------------------------- #
def init():

    return 0
    
csvFiles = traversal_files(paths, csvFiles)
data_dic = data_cleaning(csvFiles)
data_all = data_cleaning_merge(data_dic)
#获取箱线图和散点矩阵图
title = 'SL-FASPM4343A_300片'
#box_drawings(data_all,title,Box_Drawings_path)
#scatter_matrix(data_all,title,Scatter_Matrix_path)
#parm_interval_distr(data_all,title,Bar_Chart_path)
data_fun_sum(data_all,title,title,Fun_Data_path)
#data_fun_simple(data_all,title,title,Fun_Data_path)
#normal_dist(data_all,title,Normal_Distribution_path)
