# 程序初始化过程生成指定文件夹和文件
from pathlib import Path

def folder_mkdir():
    # s.find('e',-1) # 查找字符串\所在的位置
    # 获取到当前执行文件的目录，并检查是否有存在需要创建的文件夹，如果不存在则自动新建

    file_path1 = str(Path(__file__).resolve().parents[0])[:-24] + '分析报告\\CP\\'
    file_path2 = str(Path(__file__).resolve().parents[0])[:-24] + '分析报告\\FT\\'  
    file_path3 = str(Path(__file__).resolve().parents[0])[:-24] + '文件转换\\CP\\' 
    file_path4 = str(Path(__file__).resolve().parents[0])[:-24] + '文件转换\\FT\\' 
    file_path5 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Bar_Chart\\CP\\' 
    file_path6 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Bar_Chart\\FT\\'
    file_path7 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Box_Drawings\\CP\\' 
    file_path8 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Box_Drawings\\FT\\'
    file_path9 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Fun_Data\\CP\\' 
    file_path10 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Fun_Data\\FT\\'
    file_path11 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Normal_Distribution\\CP\\' 
    file_path12 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Normal_Distribution\\FT\\'
    file_path13 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Rate_Data\\CP\\' 
    file_path14 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Rate_Data\\FT\\'
    file_path15 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Scatter_Matrix\\CP\\' 
    file_path16 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Scatter_Matrix\\FT\\'
    file_path17 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Scatter_Plot\\CP\\' 
    file_path18 = str(Path(__file__).resolve().parents[0])[:-24] + '数据分析\\Scatter_Plot\\FT\\'
    file_path19 = str(Path(__file__).resolve().parents[0])[:-24] + '芯片测试数据\\'
    file_path20 = str(Path(__file__).resolve().parents[0])[:-24] + '芯片转BIN数据\\'
    file_path21 = str(Path(__file__).resolve().parents[0])[:-24] + '成品测试数据\\集佳'
    file_path22 = str(Path(__file__).resolve().parents[0])[:-24] + '成品测试数据\\升谱'
    file_path23 = str(Path(__file__).resolve().parents[0])[:-24] + '成品测试数据\\卢米斯'
    file_path24 = str(Path(__file__).resolve().parents[0])[:-24] + '成品测试数据\\佑明'


    file_paths = [file_path1,file_path2,file_path3,file_path4,file_path5,
    file_path5,file_path6,file_path7,file_path8,file_path9,file_path10,
    file_path11,file_path12,file_path13,file_path14,file_path15,file_path16,
    file_path17,file_path18,file_path19,file_path20,file_path21,file_path22,
    file_path23,file_path24]

    for path in file_paths:
        if Path(path).exists():  # 如果已经存在，则跳过并提示
	        print(path + "文件夹已经存在！")

        else:
            Path.mkdir(Path(path), parents=True, exist_ok=True)  # 创建文件夹

