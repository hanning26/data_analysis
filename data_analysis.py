import pandas as pd
import numpy as np

# 最大值，最小值，平均值，CPK，标准差，置信区间汇总
def data_fun_sum(csvDatas, title, lot_num, path, parm_columns):
    fun = pd.DataFrame()
    Fun_path = path + title + '_Fun_Data' + '.xlsx'
    for col in csvDatas.columns:
        fun_dict = {}
        data_stdev = csvDatas[col].astype(float).std()
        data_mean = csvDatas[col].astype(float).mean()
        data_max = csvDatas[col].astype(float).max()
        data_min = csvDatas[col].astype(float).min()
        data_total = csvDatas[col].count() 
        median_6Sigma1 = data_mean - 6*data_stdev
        median_6Sigma2 = data_mean + 6*data_stdev

        # 计算CPK
        for col_k in parm_columns.keys():
            if col_k == col:
                sigma = 3
                cpu = (parm_columns[col_k][1] - data_mean) / (sigma * data_stdev)
                cpl = (data_mean - parm_columns[col_k][0]) / (sigma * data_stdev)
                cpk = min(cpu, cpl)  

        fun_dict = {'lot_num':lot_num,'column':col,'stdev':data_stdev,'mean':data_mean,'max':data_max,
        'min':data_min,'total':data_total,'cpk':cpk,'median-6Sigma':median_6Sigma1,'median+6Sigma':median_6Sigma2}
        fun_dict = pd.DataFrame(fun_dict,index=[0])
        cpk = None   #清空CPK数据，防止数据重复
        fun = pd.concat([fun, fun_dict],axis=0,ignore_index=True)   
    fun.to_excel(Fun_path, sheet_name='分析汇总', encoding='utf-8', index=False)

# 最大值，最小值，平均值，标准差,Mdian±6Sigma
def data_fun_simple(csvDatas, title, lot_num, path):
    fun = pd.DataFrame()
    Fun_path = path + title +'_Fun_Data'+'_simple'+'.xlsx'
    for col in csvDatas.columns:
        print(col)
        fun_dict = {}
        data_stdev = csvDatas[col].astype(float).std()
        data_mean = csvDatas[col].astype(float).mean()
        data_max = csvDatas[col].astype(float).max()
        data_min = csvDatas[col].astype(float).min()
        data_total = csvDatas[col].count()
        median_6Sigma1 = data_mean - 6*data_stdev
        median_6Sigma2 = data_mean + 6*data_stdev
        
        fun_dict = {'lot_num':lot_num,'column':col,'stdev':data_stdev,'mean':data_mean,'max':data_max,
        'min':data_min,'total':data_total,'median-6Sigma':median_6Sigma1,'median+6Sigma':median_6Sigma2}
        fun_dict = pd.DataFrame(fun_dict,index=[0])
        fun = pd.concat([fun, fun_dict],axis=0,ignore_index=True)   
    fun.to_excel(Fun_path, sheet_name='分析汇总',encoding='utf-8',index=False)   

# 最大值，最小值，平均值，CPK，标准差，置信区间
def data_fun(csvData, col):
    fun = {}
    data_stdev = csvData.astype(float).std()
    data_mean = csvData.astype(float).mean()
    data_max = csvData.astype(float).max()
    data_min = csvData.astype(float).min()
    data_total = csvData.count() 
    # 计算CPK
    sigma = 3
    cpu = (parm_columns[col][1] - data_mean) / (sigma * data_stdev)
    cpl = (data_mean - parm_columns[col][0]) / (sigma * data_stdev)
    cpk = min(cpu, cpl)
    fun = {'column':col,'stdev':data_stdev,'mean':data_mean,'max':data_max,
    'min':data_min,'total':data_total,'cpk':cpk}
    return fun

# 求列表数据的异常点
def get_outer_data(csvData):
    # df = pd.DataFrame(csvData_list, columns=['value'])
    # csvData = csvData.iloc[:, 0]
    # 计算下四分位数和上四分位
    Q1 = csvData.quantile(q=0.25)
    Q3 = csvData.quantile(q=0.75)
    # 基于1.5倍的四分位差计算上下须对应的值
    low_whisker = Q1 - 1.5 * (Q3 - Q1)
    up_whisker = Q3 + 1.5 * (Q3 - Q1)
    # 寻找异常点
    kk = csvData[(csvData > up_whisker) | (csvData < low_whisker)]
    outlier_data = pd.DataFrame({'id': kk.index, '异常值': kk})
    return outlier_data


