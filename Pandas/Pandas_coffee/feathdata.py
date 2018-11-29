import pandas as pd
import numpy as np

df = pd.read_csv('Salary.txt', sep=',', header='infer', encoding='utf-8')
print(df)
#行/列取数

# loc()：基于标签的取数
print(df.loc[:,'Name'])#取Name这一列
print(df.loc[:,['Age','Name','Salary']])#取Name、Age、Salary这三列
print(df.loc[[0,3,5],['Age','Name','Salary']])#取第1、4、6行，同时取Name、Age、Salary这三列

#iloc()：基于索引的取数
df_1 = pd.DataFrame(np.random.randn(8,4),index= ['a','b','c','d','e','f','g','h'],columns = ['A', 'B', 'C', 'D'])
print(df_1)
print(df_1.iloc[0:4])#取前四行
print(df_1.iloc[[1,3,5],[1,3]])#取2、4、6行，第2、4列
print(df_1.iloc[1:3,:])#取2~3行，取所有得列

#基本索引运算符 [ ]
print(df['Name'])
print(df[['Name','Age','Salary']])


#增减修改

#增加一个字段“10年后的年龄”Age_10
df['Age_10'] = df['Age'] + 10
print(df)

#新建数据框df_tmp
df_tmp = df.copy()
print(df_tmp)

#删除df_tmp_1 中'Age_10'这一列.df_tmp不变,因为inplace=False
df_tmp_1 = df_tmp.drop('Age_10',axis=1,inplace=False)
print(df_tmp_1)

#inplace=True
df_tmp.drop('Age_10',axis=1,inplace=True)
print(df_tmp)