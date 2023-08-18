import csv
import os

# 获取芯片测试文件夹中文件地址
def cp_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles

# 获取芯片转BIN文件夹中文件地址
def zb_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles

# 获取集佳文件夹中文件地址
def jj_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles

# 获取升谱文件夹中文件地址
def sp_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles

# 获取卢米斯文件夹中文件地址
def lms_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles

# 获取佑明文件夹中文件地址
def ym_traversal_files(path, csvFiles):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename:
                csvFiles.append(os.path.join(folderName, filename).replace('\\','//',100))
    return csvFiles
