import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
warnings.filterwarnings("ignore")


# 根据均值、标准差,求指定范围的正态分布概率值
def norm_fun(csvData):
    x = np.arange(csvData.astype(float).min(), csvData.astype(float).max(), 0.001)
    pdf = np.exp(-((x - csvData.astype(float).mean())**2)/(2*csvData.astype(float).std()**2))/(csvData.astype(float).std() * np.sqrt(2*np.pi))
    return x, pdf
    
# 参数区间分布图绘制,可以重写if语句，根据参数规范的宽度确认bins
def parm_interval_distr(csvDatas, title, path, parm_columns):
    # bin_counts = pd.DataFrame()
    # bar_path = path + title + '_bin_counts' + '.csv'
    plt.figure()      
    for col in csvDatas.columns:
        bar_path = path + title + '_' + col + '.csv'
        bar_png_path = path + title + '_' + col + '.png'
        if col == "VF2" or col == "VF1" or col == "IR1" or col == "IR2" or col == "VF3" or col == "deltaVF":
            #参数分布区间
            bin_count = pd.DataFrame()
            # num = int((parm_columns[col][1]-parm_columns[col][0])/0.01 + 1)
            # bins = np.linspace(parm_columns[col][0],parm_columns[col][1],num).tolist()
            bins = np.arange(round(parm_columns[col][0], 2), round(parm_columns[col][1], 2), 0.01).tolist()

            # 将vf_bins列增加至data2
            bin_count[col + "_bins"] = pd.cut(x=csvDatas[col].astype(float), bins=bins, include_lowest=True, right=True, precision=3)     
            bin_count = bin_count[col + "_bins"].value_counts()
            bin_count = bin_count.to_frame(name=col + '_bins_count').reset_index()
            bin_count = bin_count[bin_count[col+ '_bins_count'] > 0]

            plt.grid(True)
            plt.xticks(rotation=70) 
            plt.bar((bin_count['index'].astype(str)),bin_count[col+ '_bins_count'])
            plt.savefig(bar_png_path, dpi=750, bbox_inches = 'tight')
            plt.show()    # 显示图表

        elif col == 'IV':
            # 参数分布区间
            bin_count = pd.DataFrame()
            # num = int((parm_columns[col][1]-parm_columns[col][0]) + 1)
            # bins = np.linspace(parm_columns[col][0],parm_columns[col][1],num).tolist()
            bins = np.arange(round(parm_columns[col][0],2),round(parm_columns[col][1],2),10).tolist()
            # 将vf_bins列增加至data2
            bin_count[col + "_bins"] = pd.cut(x=csvDatas[col].astype(float),bins=bins,include_lowest=True,right=True,precision=3)    
            bin_count = bin_count[col + "_bins"].value_counts()
            bin_count = bin_count.to_frame(name=col+'_bins_count').reset_index()
            bin_count = bin_count[bin_count[col+'_bins_count'] > 0]

            plt.grid(True)
            plt.xticks(rotation=70) 
            plt.bar((bin_count['index'].astype(str)),bin_count[col+'_bins_count'])
            plt.savefig(bar_png_path, dpi=750, bbox_inches = 'tight')
            plt.show()

        elif col == "WLD" or col == "WLP" or col == "HW":
            # 参数分布区间
            bin_count = pd.DataFrame()
            # num = int((parm_columns[col][1]-parm_columns[col][0]) + 1)
            # bins = np.linspace(parm_columns[col][0],parm_columns[col][1],num).tolist()
            bins = np.arange(round(parm_columns[col][0],2),round(parm_columns[col][1],2),1).tolist()
            # 将vf_bins列增加至data2
            bin_count[col +"_bins"] = pd.cut(x=csvDatas[col].astype(float),bins=bins,include_lowest=True,right=True,precision=3)    
            bin_count = bin_count[col +"_bins"].value_counts()
            bin_count = bin_count.to_frame(name=col+'_bins_count').reset_index()
            bin_count = bin_count[bin_count[col+'_bins_count']>0]

            plt.grid(True)
            plt.xticks(rotation=70) 
            plt.bar((bin_count['index'].astype(str)),bin_count[col+'_bins_count'])
            plt.savefig(bar_png_path, dpi=750, bbox_inches = 'tight')
            plt.show()
        #pd.concat([bin_counts, bin_count],axis=1,join='outer')
        bin_count.to_csv(bar_path)
    print('参数分布柱状图制作完成')

# 箱线图
def box_drawings(csvDatas,title,path):
    plt.figure()
    for col in csvDatas.columns:
        box_path = path + title + '_'+ col + '.jpg'
        #csvDatas[col].astype(float).to_frame().boxplot(whis=1.5)
        sns.boxplot(csvDatas[col].astype(float).to_frame(),width=0.3,fliersize=1.5,whis=1.5)
        plt.grid(True)
        plt.savefig(box_path, dpi=750, bbox_inches = 'tight')
        plt.show()

#散点图矩阵和相关性
def scatter_matrix(csvDatas,title,path):
    scatter_matrix_path = path + title + '_scatter_matrix.jpg'
    scatter_relationship_path = path + title + '_scatter_relationship.jpg'
    plt.figure(num=1,figsize=(15,9))
    #散点图矩阵
    sns.set(font_scale=1.2)
    sns.set(style="ticks", color_codes=True)
    sns.pairplot(csvDatas,diag_kind="kde",size=2.5,plot_kws={'s': 60,'alpha': 0.6,'edgecolor': 'none'})
    plt.savefig(scatter_matrix_path, bbox_inches = 'tight')
    plt.show()
    # 可视化相关系数矩阵，理论：皮尔逊相关系数
    plt.figure(num=2,figsize=(15,9))
    cm = np.corrcoef(csvDatas.values.T)
    sns.set(font_scale=1.5)
    hm = sns.heatmap(cm,
                    cbar=True,
                    annot=True,
                    square=True,
                    fmt='.2f',
                    annot_kws={'size':15},
                    yticklabels=csvDatas.columns,
                    xticklabels=csvDatas.columns)
    plt.savefig(scatter_relationship_path, bbox_inches = 'tight')
    plt.show()

#正态分布图和置信区间绘制
def normal_distribution(csvDatas,title,path): 
    for col in csvDatas.columns:
        fun = data_fun(csvDatas[col], col)
        Normal_Distribution_path = path + title + '_'+ col +'.jpg'
        # 如果所有值都相同即标准差为0则无法计算置信区间
        if fun['stdev'] == 0: 
            conf_intveral = [(fun['min'])-1, (fun['max'])+1]
        # 90%概率    
        else:
            conf_intveral = stats.norm.interval(0.9, loc=fun['mean'], scale=fun['stdev']) 
        #print('置信区间:', conf_intveral)
        # 求异常值
        outer = get_outer_data(csvDatas[col])
        # 绘制离散图
        #fig = plt.figure(figsize=(4,3),dpi=750)#创建自定义图片
        fig = plt.figure(dpi=650)
        fig.add_subplot(2, 1, 1)#将画布分成2行1列，取从左到右，从上到下第1个位置
        plt.subplots_adjust(hspace=0.3)#调整图与画布之间的间距
        x = np.arange(0, len(csvDatas[col]), 1)
        # 画所有离散点
        plt.scatter(x, csvDatas[col], s=5,marker='.', color='g',alpha=1) 
        # 画异常离散点
        plt.scatter(outer.iloc[:, 0], outer.iloc[:, 1], marker='x', color='r') 
        # 置信区间线条
        plt.plot([0, len(csvDatas[col])], [conf_intveral[0], conf_intveral[0]]) 
        # 置信区间线条
        plt.plot([0, len(csvDatas[col])], [conf_intveral[1], conf_intveral[1]]) 
        # 置信区间数字显示
        plt.text(0, conf_intveral[0], '{:.2f}'.format(conf_intveral[0])) 
        # 置信区间数字显示
        plt.text(0, conf_intveral[1], '{:.2f}'.format(conf_intveral[1]))
        info = 'outer count:{}'.format(len(outer.iloc[:, 0]))
        # 异常点数显示
        plt.text(min(x), fun['max']-((fun['max']-fun['min']) / 2), info) 
        plt.xlabel('sample count')
        plt.ylabel(title)

        # 绘制概率图
        if fun['stdev'] != 0: # 如果所有取值都相同
            fig.add_subplot(2, 1, 2)
            x,y = norm_fun(csvDatas[col])
            # 这里画出理论的正态分布概率曲线
            plt.plot(x, y) 
            # bins个柱状图,宽度是rwidth(0~1),=1没有缝隙
            plt.hist(csvDatas[col], bins=50,facecolor='blue',edgecolor="orange",rwidth=1,density=True,alpha = 0.5)
            info = 'mean:{:.2f}\nstdev:{:.2f}\nCPK:{:.2f}'.format(fun['mean'], fun['stdev'], fun['cpk'])
            plt.text(min(x), max(y) / 2, info)
            plt.xlabel(title)
            plt.ylabel('Probability')
            plt.show()

        else:
            fig.add_subplot(2, 1, 2)
            info = 'non-normal distribution!!\nmean:{:.2f}\nstd:{:.2f}\nCPK:{:.2f}'.format(fun['mean'], fun['stdev'], fun['cpk'])
            plt.text(0.5, 0.5, info)
            plt.xlabel(title)
            plt.ylabel('Probability')
            #plt.savefig('./distribution.jpg')
            plt.show()
        plt.savefig(Normal_Distribution_path, dpi=650, bbox_inches = 'tight')

#正态分布图
def normal_dist(csvDatas,title,path): 
    for col in csvDatas.columns:
        fun = data_fun(csvDatas[col], col)
        Normal_Distribution_path = path + title + '_'+ col +'.jpg'
        # 绘制概率图
        fig = plt.figure(dpi=750)
        if fun['stdev'] != 0: # 如果所有取值都相同
            fig.add_subplot(2, 1, 2)
            x,y = norm_fun(csvDatas[col])
            # 这里画出理论的正态分布概率曲线
            plt.plot(x, y) 
            # bins个柱状图,宽度是rwidth(0~1),=1没有缝隙
            plt.hist(csvDatas[col], bins=50,facecolor='blue',edgecolor="orange",rwidth=1,density=True,alpha = 0.5)
            info = 'mean:{:.2f}\nstdev:{:.2f}\nCPK:{:.2f}'.format(fun['mean'], fun['stdev'], fun['cpk'])
            plt.text(min(x), max(y) / 2, info)
            plt.xlabel(title)
            plt.ylabel('Probability')

        else:
            fig.add_subplot(2, 1, 2)
            info = 'non-normal distribution!!\nmean:{:.2f}\nstd:{:.2f}\nCPK:{:.2f}'.format(fun['mean'], fun['stdev'], fun['cpk'])
            plt.text(0.5, 0.5, info)
            plt.xlabel(title)
            plt.ylabel('Probability')
            plt.show()
        plt.savefig(Normal_Distribution_path, dpi=750, bbox_inches = 'tight')




