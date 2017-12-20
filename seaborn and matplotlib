import tushare as ts
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from string import ascii_letters
"""
python绘图笔记
"""



#产生DataFrame
testData=pd.DataFrame(np.random.normal(10,0.3,[1000,3]),columns=pd.Index(['A','B','C'],name='test'))
testData['B']+=2
testData['C']+=0.05*np.arange(1000)
print(testData.describe())

#风格设置为暗色网格
sns.set_style("darkgrid")  

f, axes = plt.subplots(3, 2, figsize=(10, 10), sharex=False)  

sns.distplot(np.random.randn(1000),bins=10, kde=True,hist=True,kde_kws={"shade": True,"color":'b'},color='k',ax=axes[0, 0])  
sns.boxplot(testData[['A','B']],orient='h',palette="PRGn",ax=axes[0, 1])  
sns.pointplot(np.arange(20),np.arange(20)+10*np.random.rand(20),linestyles='--',color='m',alpha=0.8,ax=axes[1,0])#不好用

axes[1, 1].scatter(np.arange(20),np.arange(20)+10*np.random.rand(20),color='k')
axes[2, 0].hist(np.random.randn(100),bins=10,alpha=0.5,color='g')
axes[2, 1].plot(np.arange(20),np.random.randn(20),'r--',alpha=0.5)

#双变量相关性分析，线性条件：LINE
sns.jointplot(np.arange(20),testData.iloc[:20,2],kind='reg' )


#根据矩阵里的数值大小画颜色（举例：多变量相关系数图）
f, axe3= plt.subplots(1, 1, figsize=(10, 10))  
d = pd.DataFrame(data=np.random.randn(10,26),columns=list(ascii_letters[26:]))
corr = d.corr().round(2)# 产生一个相关系数矩阵
sns.heatmap(corr,vmax=0.5,center=0,square=True, linewidths=.1, annot=False,cbar_kws={"shrink":0.6})





