# 集佳测试数据合并
from asyncio.windows_events import NULL
import csv
# from operator import inv
import os
import pandas as pd
from pathlib import Path
import datetime as dt
from dateutil.relativedelta import relativedelta
import logging  # 生成日志
import shutil  # 文件转移
import numpy as np
import sys
import time
# ft_paths:测试数据，rt_paths:不良品复测数据,data_merge_paths:合并数据地址
# invalid_folder_paths:异常数据存放地址
ft_paths1 = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\FT').replace('\\', '//')
rt_paths1 = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\RT').replace('\\', '//')
ft_paths2 = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\历史备份\FT').replace('\\', '//')
rt_paths2 = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\历史备份\RT').replace('\\', '//')
data_merge_paths = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\合并数据').replace('\\', '//')
invalid_folder_paths = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\无效文件').replace('\\', '//')
history_backup_paths = (r'C:\Users\hanning\Desktop\光电产品数据分析\Data_Processing_Software\data_merge\历史备份').replace('\\', '//')
ft = (r'\\172.17.1.212\FCTRecords\106-LED\标普设备\测试数据\RT')

ft_product_names = []  # 成品名称
rt_product_names = []  # 复测成品名称
ft_chip_names = []  # 芯片名称
rt_chip_names = []  # 复测芯片名称 
ft_names_dict = {}  # 测试数据的名称与每个下划线字段的字典
rt_names_dict = {}  # 不良品复测数据名称与每个下划线字段的字典

ft_now_csvFiles1 = []
ft_last_csvFiles1 = []   # 初始化得到的本月和上个月的文件名列表
rt_now_csvFiles1 = []
rt_last_csvFiles1 = []
ft_now_csvFiles2 = []
ft_last_csvFiles2 = []    # 正式运行得到的本月和上个月的文件名列表
rt_now_csvFiles2 = []
rt_last_csvFiles2 = []
# 获取现在和过去的月份
class DateTimeUtil():
    def get_cur_month(self):
        # 获取当前年，月
        return dt.datetime.now().strftime('%Y'), dt.datetime.now().strftime("%Y_%m")

    def get_last_month(self, number=1):
        # 获取前几个月
        month_date = dt.datetime.now().date() - relativedelta(months=number)
        return month_date.strftime("%Y_%m")

# 生成进度条
def progressbar():
    # sys.stdout.write()方法跟print()方法的区别是 前者打印不换行，后者换行。
    # sys.stdout.flush()方法是立即刷新输出的内容  
    for i in range(11):
        if i != 10:
            sys.stdout.write("==")
        else:
            sys.stdout.write("== " + str(i * 10) + "%/100%")
        sys.stdout.flush()
        time.sleep(0.2)

# 根据时间创建文件夹
def create_time_folder(path):
    # 年-月-日 时：分：秒
    now_time = dt.datetime.now().strftime("%Y_%m_%d %H:%M:%S")
    # 年
    year = dt.datetime.now().strftime('%Y')
    # 年-月
    month = dt.datetime.now().strftime('%Y_%m')
    # 年-月-日
    day = dt.datetime.now().strftime('%Y_%m_%d')
    # 时：分：秒
    hour = dt.datetime.now().strftime("%H:%M:%S")
    # print(now_time + "\n" + day + "\n" + hour)
    # 创建时间到月的文件夹
    # foldername = path + "\\" + year + "\\" + month + "\\" + day
    foldername = path + "\\" + year + "\\" + month + "\\"
    day_time = day
    # 文件路径
    word_name = os.path.exists(foldername)
    # 判断文件是否存在：不存在创建
    if not word_name:
        os.makedirs(foldername)
    # 返回创建的文件夹地址
    return foldername, day_time

# 创建文件夹
def create_folder(path):
    # 文件路径
    word_name = os.path.exists(path)
    # 判断文件是否存在：不存在创建
    if not word_name:
        os.makedirs(path)

# 获取集佳FT+RT文件夹中文件地址
def jj_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles

# 识别字符串是否包含中文
def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# 异常文件识别函数
def exception_file_recognition(file_path):
    # 获取文件地址和名称(不带路径)
    loc1 = file_path.rfind('//')
    loc2 = file_path.rfind('.')
    ft_name_file = file_path[loc1 + 2:loc2]
    # 异常文件转移到无效文件
    if ft_name_file.count('_') != 7:
        logging.error(ft_name_file + ':文件名格式错误')
        invalid_foldername, invalid_time = create_folder(invalid_folder_paths)
        shutil.move(file_path, invalid_foldername)
        return 1
    if (file_path.rfind('副本') > 0) | (file_path.upper().rfind('XLS') > 0):
        logging.error(ft_name_file + ':文件名格式错误')
        invalid_foldername, invalid_time = create_folder(invalid_folder_paths)
        shutil.move(file_path, invalid_foldername)
        return 1
    if (file_path.upper().rfind('.CSV') - file_path.rfind(')')) < 3:
        logging.error(ft_name_file + ':文件名重复')
        invalid_foldername, invalid_time = create_folder(invalid_folder_paths)
        shutil.move(file_path, invalid_foldername)
        return 1
    if is_chinese(ft_name_file) == 1:
        logging.error(ft_name_file + ':文件名包含中文')
        invalid_foldername, invalid_time = create_folder(invalid_folder_paths)
        shutil.move(file_path, invalid_foldername)        
        return 1
    # 判断文件内容是否有问题
    temp = []
    with open(file_path, 'r', encoding='gbk') as f_input:
        for line in f_input:
            temp.append(list(line.strip().split(',')))
        dataset = pd.DataFrame(temp)
        # dataset1 = dataset.iloc[0:12,:].copy()
        dataset1 = dataset.iloc[12:, :].copy()
    dataset2 = dataset1[5].str.contains('PASS|NG', case=False)
    for i in dataset2:
        if i != 1: 
            logging.error(ft_name_file + ':文件中存在异常数据')
            invalid_foldername, invalid_time = create_time_folder(invalid_folder_paths)
            shutil.move(file_path, invalid_foldername)        
            return 1

# 创建程序运行日志(按时间生成对应文件夹)
def app_log():
    year_file_path = str(Path(__file__).resolve().parents[0]) + '\\log\\'
    log_foldername, log_time = create_time_folder(year_file_path)
    log_file = log_foldername + '\\' + log_time + '.log'
    logging.basicConfig(level=logging.INFO,
                        filename=log_file,
                        filemode='w',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 在合并\\FT/RT文件夹中创建每月的文件夹并将文件按月份区分
def year_folder():
    ft_csvFiles = []   # 测试数据地址列表
    rt_csvFiles = []   # 复测数据地址列表
    
    ft_csvFiles = jj_traversal_files(ft_paths1, ft_csvFiles)  # 获取文件列表中的文件
    rt_csvFiles = jj_traversal_files(rt_paths1, rt_csvFiles)  # 获取文件列表中的文件
    # 文件分选
    try:    
        # 处理测试数据
        ft_time_names = []
        for ft_csvFile in ft_csvFiles:
            # 获取文件地址和名称(不带路径)
            loc1 = ft_csvFile.rfind('//')
            loc2 = ft_csvFile.rfind('.')
            ft_name_file = ft_csvFile[loc1 + 2:loc2]
            # 异常文件转移到无效文件夹
            if exception_file_recognition(ft_csvFile) == 1:
                continue
            ft_name_list = ft_name_file.split('_')  # 获取文件名中的各个字段信息
            ft_time_names = ft_name_list[7].strip()
            # 创建FT月份文件夹
            year_ft_path = history_backup_paths + '\\FT\\' + ft_time_names[0:4] \
                + '\\' + ft_time_names[0:4] + '_' + ft_time_names[4:6]
            create_folder(year_ft_path)
            # 提取FT文件到月份文件夹
            shutil.move(ft_csvFile, year_ft_path)
        # 处理复测数据
        rt_time_names = []
        for rt_csvFile in rt_csvFiles:
            rt_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
            # 获取文件地址和名称(不带路径)
            loc1 = rt_csvFile.rfind('//')
            loc2 = rt_csvFile.rfind('.')
            rt_name_file = rt_csvFile[loc1 + 2:loc2]
            # 异常文件转移到无效文件
            if exception_file_recognition(rt_csvFile) == 1:
                continue
            rt_name_list = rt_name_file.split('_')
            rt_time_names = rt_name_list[7].strip()
            # 创建RT月份文件夹
            year_rt_path = history_backup_paths + '\\RT\\' + rt_time_names[0:4] \
                + '\\' + rt_time_names[0:4] + '_' + rt_time_names[4:6]
            create_folder(year_rt_path)
            # 提取RT文件到月份文件夹 
            shutil.move(rt_csvFile, year_rt_path)

        if ft_csvFiles == [] or rt_csvFiles == []:
            return 1
    except Exception as e:
        logging.info('数据分类错误信息：' + e)    # 如果出现错误，则显示错误信息。
        pass

# 数据合并
def data_merge(ft_csvFile, rt_csvFile, merge_data):
    ft_temp = []   # 清空数据列表，防止数据累加和溢出
    try:
        if merge_data.empty:
            with open(ft_csvFile, 'r', encoding='gbk') as f_input:  
                for line in f_input:
                    ft_temp.append(list(line.strip().split(',')))
                ft_dataset = pd.DataFrame(ft_temp)
                ft_dataset1 = ft_dataset.iloc[0:12, :].copy()  # 筛选前12行
                ft_dataset2 = ft_dataset.iloc[12:, :].copy()  # 筛选12行之后的数据
                ft_dataset2 = ft_dataset2.loc[ft_dataset2[5].str.contains('PASS', case=False)]
                # ft_dataset.reset_index(inplace=True,drop=True)
                # dataset = dataset.dropna(thresh=100, axis=1, inplace=False) #去除空值行sv(path).copy()
                print(ft_dataset)
            # 读取RT数据
            rt_temp = []   # 清空数据列表，防止数据累加和溢出
            with open(rt_csvFile, 'r', encoding='gbk') as f_input:
                for line in f_input:
                    rt_temp.append(list(line.strip().split(',')))
                rt_dataset = pd.DataFrame(rt_temp)
                rt_dataset1 = rt_dataset.iloc[0:12, :].copy()  # 筛选前12行
                rt_dataset2 = rt_dataset.iloc[12:, :].copy()  # 筛选12行之后的数据
    
            # 将FT和RT数据通过connect合并
            ft_dataset1 = pd.concat([ft_dataset1, ft_dataset2], axis=0, ignore_index=True)
            ft_dataset1 = pd.concat([ft_dataset1, rt_dataset2], axis=0, ignore_index=True)
            return ft_dataset1
        else:
            # 合并过后的FT数据
            merge_data1 = merge_data.iloc[0:12, :].copy()  # 筛选前12行
            merge_data2 = merge_data.iloc[12:, :].copy()  # 筛选12行之后的数据
            merge_data2 = merge_data2.loc[merge_data2[5].str.contains('PASS', case=False)]

            # 读取RT数据
            rt_temp = []   # 清空数据列表，防止数据累加和溢出
            with open(rt_csvFile, 'r', encoding='gbk') as f_input:
                for line in f_input:
                    rt_temp.append(list(line.strip().split(',')))
                rt_dataset = pd.DataFrame(rt_temp)
                rt_dataset1 = rt_dataset.iloc[0:12, :].copy()  # 筛选前12行
                rt_dataset2 = rt_dataset.iloc[12:, :].copy()  # 筛选12行之后的数据
            # 将FT和RT数据通过connect合并
            merge_data1 = pd.concat([merge_data1, merge_data2], axis=0, ignore_index=True)
            merge_data1 = pd.concat([merge_data1, rt_dataset2], axis=0, ignore_index=True)
            return merge_data1
    except Exception as e:
        logging.info('数据合并错误信息：' + e)    # 如果出现错误，则显示错误信息。
        pass

# 将获取到的测试数据分类
def get_data_type():
    ft_csvFiles = []   # 测试数据地址列表
    rt_csvFiles = []   # 复测数据地址列表
    ft_csvFiles = jj_traversal_files(ft_paths2, ft_csvFiles)  # 获取文件列表中的文件
    rt_csvFiles = jj_traversal_files(rt_paths2, rt_csvFiles)  # 获取文件列表中的文件
    try:    
        # 处理测试数据
        ft_batch_name = []
        ft_batch_names = []
        for ft_csvFile in ft_csvFiles:
            ft_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
            # 获取文件地址和名称(不带路径)
            loc1 = ft_csvFile.rfind('//')
            loc2 = ft_csvFile.rfind('.')
            ft_name_file = ft_csvFile[loc1 + 2:loc2]
            # 将获取到的文件名拆分
            ft_name_list = ft_name_file.upper().split('_')  # 获取文件名中的各个字段信息
            ft_batch_name.append(ft_name_list[4])  # 获取批号名称
            ft_name_dict['成品名称'] = ft_name_list[0].strip()
            ft_name_dict['芯片名称'] = ft_name_list[1].strip()
            ft_name_dict['NA'] = ft_name_list[2].strip()
            ft_name_dict['印章批号'] = ft_name_list[3].strip()
            ft_name_dict['测试批号'] = ft_name_list[4].strip()
            ft_name_dict['测试代号'] = ft_name_list[5].strip()
            ft_name_dict['机台编号'] = ft_name_list[6].strip()
            ft_name_dict['时间'] = ft_name_list[7].strip()
            ft_names_dict[ft_csvFile] = ft_name_dict
        ft_batch_names = list(set(ft_batch_name))    # 去除重复批号名称

        # 处理复测数据
        rt_batch_name = []
        rt_batch_names = []
        for rt_csvFile in rt_csvFiles:
            rt_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
            # 获取文件地址和名称(不带路径)
            loc1 = rt_csvFile.rfind('//')
            loc2 = rt_csvFile.rfind('.')
            rt_name_file = rt_csvFile[loc1 + 2:loc2]
            # 将获取到的文件名拆分
            rt_name_list = rt_name_file.upper().split('_')
            rt_batch_name.append(rt_name_list[4])  # 获取复测批号名称
            rt_name_dict['成品名称'] = rt_name_list[0].strip()
            rt_name_dict['芯片名称'] = rt_name_list[1].strip()
            rt_name_dict['NA'] = rt_name_list[2].strip()
            rt_name_dict['印章批号'] = rt_name_list[3].strip()
            rt_name_dict['测试批号'] = rt_name_list[4].strip()
            rt_name_dict['测试代号'] = rt_name_list[5].strip()
            rt_name_dict['机台编号'] = rt_name_list[6].strip()
            rt_name_dict['时间'] = rt_name_list[7].strip()
            rt_names_dict[rt_csvFile] = rt_name_dict
        rt_batch_names = list(set(rt_batch_name))    # 去除重复批号名称

        # 合并FT+RT数据(两种情况 1:FT数据没有RT数据,直接将数据copy到合并文件夹)
        # 2:FT数据有RT数据，将FT与RT数据合并放到合并文件夹)
        num = 0 
        batch_count = {}    # 确认FT数据是否有与其对应的RT数据
        ft_rt_map1 = {}  # 找到所有FT数据与其对应的RT数据 
        ft_rt_map2 = {}  # 存放RT数据的测试代号
        # 可以考虑再次优化，将FT2数据没有RT数据的直接复制      
        for ft_batch in ft_batch_names:
            for rt_batch in rt_batch_names: 
                if (rt_batch == ft_batch):
                    num += 1
            batch_count[ft_batch] = num
            num = 0   # num变量必须清零
        for ft_name, ft_value in ft_names_dict.items():
            if (batch_count[ft_value['测试批号']] == 0):
                shutil.copy(ft_name, data_merge_paths)
                continue
            else:
                # 找到与FT数据对应的RT数据集合
                rt_list = []  # 汇总相同的RT数据
                rt_code_list = []   # 汇总相同RT数据的测试代号
                for rt_name, rt_value in rt_names_dict.items():
                    if ft_value['测试代号'][-2:] == rt_value['测试代号'][-2:] and ft_value['印章批号'] == rt_value['印章批号'] and ft_value['测试批号'] == rt_value['测试批号']:
                        rt_list.append(rt_name)
                        rt_code_list.append(rt_value['测试代号'])
                ft_rt_map1[ft_name] = rt_list
                ft_rt_map2[ft_name] = rt_code_list
        # 对ft_rt_map里的数据进行合并
        for ft_rt_key, ft_rt_value in ft_rt_map1.items():
            # 判断FT数据是否存在对应的RT数据,没有直接复制FT数据到合并数据
            if ft_rt_map2[ft_rt_key] == []:
                shutil.copy(ft_rt_key, data_merge_paths)
                continue
            rt_code_list = ft_rt_map2[ft_rt_key]
            rt_code_list.sort(reverse=True)
            # rt_code = max(ft_rt_map2[ft_rt_key], key=len, default='') 获取列表中最长的字符串
            for rt_value in rt_code_list:
                merge_data = pd.DataFrame()    # 存放合并的数据
                loc1 = ft_rt_key.rfind('//')
                loc2 = ft_rt_key.rfind('.')
                ft_name_file = ft_rt_key[loc1 + 2:loc2]  #获得文件不带地址的名称
                for rt_name in ft_rt_value:
                    # 存在RT1前面有空格的情况
                    if rt_name.find('_' + rt_value) > 0:
                        # FT+RT合并
                        # 将FT文件路径和RT路径传入数据合并函数
                        merge_data = data_merge(ft_rt_key, rt_name, merge_data)
                # 生成合并文件
                merge_data.to_csv(data_merge_paths + '//' + ft_name_file + '.CSV', encoding='utf_8_sig', index=False, header=None)

    except Exception as e:
        logging.info('数据分类错误信息：' + e)    # 如果出现错误，则显示错误信息。
        pass

# 程序初始化
def init():
    global ft_now_csvFiles1, ft_last_csvFiles1, ft_now_csvFiles2, ft_last_csvFiles2
    app_log()
    year_folder()
    get_data_type()
    now_year1, now_mouth1 = DateTimeUtil().get_cur_month()
    last_month1 = DateTimeUtil().get_last_month(1)
    ft_now_path1 = ft_paths2 + '//' + now_year1 + '//' + now_mouth1 + '//'
    ft_last_path1 = ft_paths2 + '//' + now_year1 + '//' + last_month1 + '//'
    rt_now_path1 = rt_paths2 + '//' + now_year1 + '//' + now_mouth1 + '//'
    rt_last_path1 = rt_paths2 + '//' + now_year1 + '//' + last_month1 + '//'

    # 拼接FT文件名和地址
    ft_now_path_list1 = os.listdir(ft_now_path1)
    for filename in ft_now_path_list1:
        if filename:
            ft_now_csvFiles1.append(os.path.join(ft_now_path1, filename).replace('\\', '//', 100))
    ft_last_path_list1 = os.listdir(ft_last_path1)
    for filename in ft_last_path_list1:
        if filename:
            ft_last_csvFiles1.append(os.path.join(ft_last_path1, filename).replace('\\', '//', 100))

    # 拼接RT文件名和地址
    rt_now_path_list1 = os.listdir(rt_now_path1)
    for filename in rt_now_path_list1:
        if filename:
            rt_now_csvFiles1.append(os.path.join(rt_now_path1, filename).replace('\\', '//', 100))
    rt_last_path_list1 = os.listdir(rt_last_path1)
    for filename in rt_last_path_list1:
        if filename:
            rt_last_csvFiles1.append(os.path.join(rt_last_path1, filename).replace('\\', '//', 100))            

def merge_main():
    app_log()
    if year_folder() != 1:
        # 获取RT的更新数据
        rt_now_file_list = []   # 保存本月更新的文件集合
        rt_last_file_list = []  # 保存上个月更新的文件集合
        ft_now_file_list = []   # 保存本月更新的文件集合
        ft_last_file_list = []  # 保存上个月更新的文件集合
        now_year2, now_mouth2 = DateTimeUtil().get_cur_month()
        last_month2 = DateTimeUtil().get_last_month(1)
        rt_now_path2 = rt_paths2 + '//' + now_year2 + '//' + now_mouth2 + '//'
        rt_last_path2 = rt_paths2 + '//' + now_year2 + '//' + last_month2 + '//'
        ft_now_path2 = ft_paths2 + '//' + now_year2 + '//' + now_mouth2 + '//'
        ft_last_path2 = ft_paths2 + '//' + now_year2 + '//' + last_month2 + '//'
        # 拼接文件名和地址
        rt_now_path_list2 = os.listdir(rt_now_path2)
        for filename in rt_now_path_list2:
            if filename:
                rt_now_csvFiles2.append(os.path.join(rt_now_path2, filename).replace('\\', '//', 100))
        rt_last_path_list2 = os.listdir(rt_last_path2)

        for filename in rt_last_path_list2:
            if filename:
                rt_last_csvFiles2.append(os.path.join(rt_last_path2, filename).replace('\\', '//', 100))
        
        rt_now_file_list = list(set(rt_now_csvFiles2).difference(set(rt_now_csvFiles1)))
        rt_last_file_list = list(set(rt_last_csvFiles2).difference(set(rt_last_csvFiles1)))
        rt_differ_file_lists = rt_now_file_list + rt_last_file_list  # 获得更新后的数据
        rt_and_file_lists = rt_now_csvFiles2 + rt_last_csvFiles2    # 获得所有数据
        # 获取FT的更新数据
        ft_now_path_list2 = os.listdir(ft_now_path2)
        # 拼接文件名和地址
        for filename in ft_now_path_list2:
            if filename:
                ft_now_csvFiles2.append(os.path.join(ft_now_path2, filename).replace('\\', '//', 100))
        ft_last_path_list2 = os.listdir(ft_last_path2)
        for filename in ft_last_path_list2:
            if filename:
                ft_last_csvFiles2.append(os.path.join(ft_last_path2, filename).replace('\\', '//', 100))
        ft_now_file_list = list(set(ft_now_csvFiles2).difference(set(ft_now_csvFiles1)))
        ft_last_file_list = list(set(ft_last_csvFiles2).difference(set(ft_last_csvFiles1)))
        ft_differ_file_lists = ft_now_file_list + ft_last_file_list   # 获得差异的数据
        ft_and_file_lists = ft_now_csvFiles2 + ft_last_csvFiles2
        # 获得到更新的RT文件需要遍历本月和上个月的数据
        try: 
            if  rt_differ_file_lists != []:          
                # 处理测试数据
                ft_batch_name = []
                ft_batch_names = []
                for ft_csvFile in ft_and_file_lists:
                    ft_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
                    # 获取文件地址和名称(不带路径)
                    loc1 = ft_csvFile.rfind('//')
                    loc2 = ft_csvFile.rfind('.')
                    ft_name_file = ft_csvFile[loc1 + 2:loc2]
                    # 将获取到的文件名拆分
                    ft_name_list = ft_name_file.upper().split('_')  # 获取文件名中的各个字段信息
                    ft_batch_name.append(ft_name_list[4])  # 获取批号名称
                    ft_name_dict['成品名称'] = ft_name_list[0].strip()
                    ft_name_dict['芯片名称'] = ft_name_list[1].strip()
                    ft_name_dict['NA'] = ft_name_list[2].strip()
                    ft_name_dict['印章批号'] = ft_name_list[3].strip()
                    ft_name_dict['测试批号'] = ft_name_list[4].strip()
                    ft_name_dict['测试代号'] = ft_name_list[5].strip()
                    ft_name_dict['机台编号'] = ft_name_list[6].strip()
                    ft_name_dict['时间'] = ft_name_list[7].strip()
                    ft_names_dict[ft_csvFile] = ft_name_dict
                ft_batch_names = list(set(ft_batch_name))    # 去除重复批号名称
                # 处理复测数据
                rt_batch_name = []
                rt_batch_names = []
                for rt_csvFile in rt_differ_file_lists:
                    rt_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
                    # 获取文件地址和名称(不带路径)
                    loc1 = rt_csvFile.rfind('//')
                    loc2 = rt_csvFile.rfind('.')
                    rt_name_file = rt_csvFile[loc1 + 2:loc2]
                    # 将获取到的文件名拆分
                    rt_name_list = rt_name_file.upper().split('_')
                    rt_batch_name.append(rt_name_list[4])  # 获取复测批号名称
                    rt_name_dict['成品名称'] = rt_name_list[0].strip()
                    rt_name_dict['芯片名称'] = rt_name_list[1].strip()
                    rt_name_dict['NA'] = rt_name_list[2].strip()
                    rt_name_dict['印章批号'] = rt_name_list[3].strip()
                    rt_name_dict['测试批号'] = rt_name_list[4].strip()
                    rt_name_dict['测试代号'] = rt_name_list[5].strip()
                    rt_name_dict['机台编号'] = rt_name_list[6].strip()
                    rt_name_dict['时间'] = rt_name_list[7].strip()
                    rt_names_dict[rt_csvFile] = rt_name_dict
                rt_batch_names = list(set(rt_batch_name))    # 去除重复批号名称
                
                # 合并FT+RT数据(两种情况 1:FT数据没有RT数据,直接将数据copy到合并文件夹)
                # 2:FT数据有RT数据，将FT与RT数据合并放到合并文件夹)
                num = 0 
                batch_count = {}    # 确认FT数据是否有与其对应的RT数据
                ft_rt_map1 = {}  # 找到所有FT数据与其对应的RT数据 
                ft_rt_map2 = {}  # 存放RT数据的测试代号
                # 可以考虑再次优化，将FT2数据没有RT数据的直接复制      
                for ft_batch in ft_batch_names:
                    for rt_batch in rt_batch_names: 
                        if (rt_batch == ft_batch):
                            num += 1
                    batch_count[ft_batch] = num
                    num = 0   # num变量必须清零
                for ft_name, ft_value in ft_names_dict.items():
                    if (batch_count[ft_value['测试批号']] == 0):
                        shutil.copy(ft_name, data_merge_paths)
                        continue
                    else:
                        # 找到与FT数据对应的RT数据集合
                        rt_list = []  # 汇总相同的RT数据
                        rt_code_list = []   # 汇总相同RT数据的测试代号
                        for rt_name, rt_value in rt_names_dict.items():
                            if ft_value['测试代号'][-2:] == rt_value['测试代号'][-2:] and ft_value['印章批号'] == rt_value['印章批号'] and ft_value['测试批号'] == rt_value['测试批号']:
                                rt_list.append(rt_name)
                                rt_code_list.append(rt_value['测试代号'])
                        ft_rt_map1[ft_name] = rt_list
                        ft_rt_map2[ft_name] = rt_code_list
                # 对ft_rt_map里的数据进行合并
                for ft_rt_key, ft_rt_value in ft_rt_map1.items():
                    # 判断FT数据是否存在对应的RT数据,没有直接复制FT数据到合并数据
                    if ft_rt_map2[ft_rt_key] == []:
                        shutil.copy(ft_rt_key, data_merge_paths)
                        continue
                    rt_code_list = ft_rt_map2[ft_rt_key]
                    rt_code_list.sort(reverse=True)
                    # rt_code = max(ft_rt_map2[ft_rt_key], key=len, default='') 获取列表中最长的字符串
                    for rt_value in rt_code_list:
                        merge_data = pd.DataFrame()    # 存放合并的数据
                        loc1 = ft_rt_key.rfind('//')
                        loc2 = ft_rt_key.rfind('.')
                        ft_name_file = ft_rt_key[loc1 + 2:loc2]  #获得文件不带地址的名称
                        for rt_name in ft_rt_value:
                            # 存在RT1前面有空格的情况
                            if rt_name.find('_' + rt_value) > 0:
                                # FT+RT合并
                                # 将FT文件路径和RT路径传入数据合并函数
                                merge_data = data_merge(ft_rt_key, rt_name, merge_data)
                        # 生成合并文件
                        merge_data.to_csv(data_merge_paths + '//' + ft_name_file + '.CSV', encoding='utf_8_sig', index=False, header=None)

            if  ft_differ_file_lists != []:
                # 处理测试数据
                ft_batch_name = []
                ft_batch_names = []
                for ft_csvFile in ft_differ_file_lists:
                    ft_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
                    # 获取文件地址和名称(不带路径)
                    loc1 = ft_csvFile.rfind('//')
                    loc2 = ft_csvFile.rfind('.')
                    ft_name_file = ft_csvFile[loc1 + 2:loc2]
                    # 将获取到的文件名拆分
                    ft_name_list = ft_name_file.upper().split('_')  # 获取文件名中的各个字段信息
                    ft_batch_name.append(ft_name_list[4])  # 获取批号名称
                    ft_name_dict['成品名称'] = ft_name_list[0].strip()
                    ft_name_dict['芯片名称'] = ft_name_list[1].strip()
                    ft_name_dict['NA'] = ft_name_list[2].strip()
                    ft_name_dict['印章批号'] = ft_name_list[3].strip()
                    ft_name_dict['测试批号'] = ft_name_list[4].strip()
                    ft_name_dict['测试代号'] = ft_name_list[5].strip()
                    ft_name_dict['机台编号'] = ft_name_list[6].strip()
                    ft_name_dict['时间'] = ft_name_list[7].strip()
                    ft_names_dict[ft_csvFile] = ft_name_dict
                ft_batch_names = list(set(ft_batch_name))    # 去除重复批号名称
                # 处理复测数据
                rt_batch_name = []
                rt_batch_names = []
                for rt_csvFile in rt_and_file_lists:
                    rt_name_dict = {}  # 必须在循环中创建局部变量，否则会导致字典中数据重复
                    # 获取文件地址和名称(不带路径)
                    loc1 = rt_csvFile.rfind('//')
                    loc2 = rt_csvFile.rfind('.')
                    rt_name_file = rt_csvFile[loc1 + 2:loc2]
                    # 将获取到的文件名拆分
                    rt_name_list = rt_name_file.upper().split('_')
                    rt_batch_name.append(rt_name_list[4])  # 获取复测批号名称
                    rt_name_dict['成品名称'] = rt_name_list[0].strip()
                    rt_name_dict['芯片名称'] = rt_name_list[1].strip()
                    rt_name_dict['NA'] = rt_name_list[2].strip()
                    rt_name_dict['印章批号'] = rt_name_list[3].strip()
                    rt_name_dict['测试批号'] = rt_name_list[4].strip()
                    rt_name_dict['测试代号'] = rt_name_list[5].strip()
                    rt_name_dict['机台编号'] = rt_name_list[6].strip()
                    rt_name_dict['时间'] = rt_name_list[7].strip()
                    rt_names_dict[rt_csvFile] = rt_name_dict
                rt_batch_names = list(set(rt_batch_name))    # 去除重复批号名称
                # 合并FT+RT数据(两种情况 1:FT数据没有RT数据,直接将数据copy到合并文件夹)
                # 2:FT数据有RT数据，将FT与RT数据合并放到合并文件夹)
                num = 0
                batch_count = {}    # 确认FT数据是否有与其对应的RT数据
                ft_rt_map1 = {}  # 找到所有FT数据与其对应的RT数据 
                ft_rt_map2 = {}  # 存放RT数据的测试代号
                # 可以考虑再次优化，将FT2数据没有RT数据的直接复制      
                for ft_batch in ft_batch_names:
                    for rt_batch in rt_batch_names: 
                        if (rt_batch == ft_batch):
                            num += 1
                    batch_count[ft_batch] = num
                    num = 0   # num变量必须清零
                for ft_name, ft_value in ft_names_dict.items():
                    if (batch_count[ft_value['测试批号']] == 0):
                        shutil.copy(ft_name, data_merge_paths)
                        continue
                    else:
                        # 找到与FT数据对应的RT数据集合
                        rt_list = []  # 汇总相同的RT数据
                        rt_code_list = []   # 汇总相同RT数据的测试代号
                        for rt_name, rt_value in rt_names_dict.items():
                            if ft_value['测试代号'][-2:] == rt_value['测试代号'][-2:] and ft_value['印章批号'] == rt_value['印章批号'] and ft_value['测试批号'] == rt_value['测试批号']:
                                rt_list.append(rt_name)
                                rt_code_list.append(rt_value['测试代号'])
                        ft_rt_map1[ft_name] = rt_list
                        ft_rt_map2[ft_name] = rt_code_list
                # 对ft_rt_map里的数据进行合并
                for ft_rt_key, ft_rt_value in ft_rt_map1.items():
                    # 判断FT数据是否存在对应的RT数据,没有直接复制FT数据到合并数据
                    if ft_rt_map2[ft_rt_key] == []:
                        shutil.copy(ft_rt_key, data_merge_paths)
                        continue
                    rt_code_list = ft_rt_map2[ft_rt_key]
                    rt_code_list.sort(reverse=True)
                    # rt_code = max(ft_rt_map2[ft_rt_key], key=len, default='') 获取列表中最长的字符串
                    for rt_value in rt_code_list:
                        merge_data = pd.DataFrame()    # 存放合并的数据
                        loc1 = ft_rt_key.rfind('//')
                        loc2 = ft_rt_key.rfind('.')
                        ft_name_file = ft_rt_key[loc1 + 2:loc2]  #获得文件不带地址的名称
                        for rt_name in ft_rt_value:
                            # 存在RT1前面有空格的情况
                            if rt_name.find('_' + rt_value) > 0:
                                # FT+RT合并
                                # 将FT文件路径和RT路径传入数据合并函数
                                merge_data = data_merge(ft_rt_key, rt_name, merge_data)
                        # 生成合并文件
                        merge_data.to_csv(data_merge_paths + '//' + ft_name_file + '.CSV', encoding='utf_8_sig', index=False, header=None)

            # 程序最后将更新后的文件复制
            ft_now_csvFiles1 = ft_now_csvFiles2
            ft_last_csvFiles1 = ft_last_csvFiles2
            rt_now_csvFiles1 = rt_now_csvFiles2
            rt_last_csvFiles1 = rt_last_csvFiles2
        except Exception as e:
            logging.info('数据分类错误信息：' + e)    # 如果出现错误，则显示错误信息。
            pass

init()
time.sleep(20)
merge_main()    
    
    


