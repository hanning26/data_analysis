import pandas as pd
import os

#数据清洗+并将每批数据保存到字典
def data_cleaning(csvFiles,data_conversion_columns,data_columns):
    temp = []
    for csvFile in csvFiles: 
        #获取文件地址和名称(不带路径) 
        loc1 = csvFile.rfind('//')
        loc2 = csvFile.rfind('.')
        name_file = csvFile[loc1+2:loc2]  
        #针对明镓csv格式异常数据特殊处理
        with open(csvFile, 'r',encoding='utf-8-sig') as f_input:
            for line in f_input:
                temp.append(list(line.strip().split(',')))
        dataset=pd.DataFrame(temp,dtype=float)
        temp = []     #清空数据列表，防止数据累加和溢出
        dataset = dataset.iloc[54:,:].copy()#行筛选
        dataset.columns = dataset.iloc[0,:]
        dataset.reset_index(inplace=True,drop=True)
        dataset = dataset.dropna(thresh=100, axis=1, inplace=False) #去除空值行sv(path).copy()
        dataset.drop(index=[0],inplace=True)
        dataset = dataset.drop(labels=drop_col, axis=1)
        dataset[data_conversion_columns] = dataset[data_conversion_columns].astype('float')
        dataset.columns = data_columns
        #缺少LOP3
        dataset = dataset.loc[(dataset['VF1']>=2.8)&(dataset['VF1']<=3.3)&(dataset['VF2']>=2.2)&(dataset['VF2']<=2.4)
        &(dataset['VF3']>=2.6)&(dataset['VF3']<=2.8)&(dataset['VFD']>=0)&(dataset['VFD']<=0.05)&(dataset['LOP1']>=1040)&(dataset['LOP1']<=1300)&
        (dataset['WLP1']>=430)&(dataset['WLP1']<=470)&(dataset['HW1']>=14)&(dataset['HW1']<=21)&(dataset['WLD1']>=445)&(dataset['WLD1']<=465)&
        (dataset['WLP3']>=430)&(dataset['WLP3']<=470)&(dataset['HW3']>=14)&(dataset['HW3']<=21)&(dataset['WLD3']>=445)&(dataset['WLD3']<=465)&
        (dataset['IR']>=0)&(dataset['IR']<=0.05)&(dataset['IR2']>=0)&(dataset['IR2']<=0.05)&(dataset['IR3']>=0)&(dataset['IR3']<=0.05)]
        dataset.to_csv(data_conversion_paths + '//' + name_file +'.csv')
        data_dic[name_file] = dataset
    return data_dic

#数据清洗+合并
def data_cleaning_merge(data_dic):
    temp = []
    csvdatas = pd.DataFrame()
    for key in data_dic.keys(): 
        csvdatas = pd.concat([csvdatas, data_dic[key]],axis=0,ignore_index=True) 

    #csvdatas.to_csv(data_conversion_paths + '//' + '300片汇总数据' +'.csv')     
    return csvdatas

#数据转换并生成csv文件
def data_convert_to_csv(data_dic, data_conversion_paths):
    for k,v in data_dic.items():
        v.to_csv(data_conversion_paths + '//' + k +'.csv')