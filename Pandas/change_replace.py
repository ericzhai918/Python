import pandas as pd
import numpy as np

df_2 = pd.read_csv('Salary_2.txt', sep=',', header='infer',encoding = 'utf-8')

#常量填补
df_2.fillna(-1)

#字符串填补
df_2.fillna('missing')

#用每列中最大值填补每列中的NA缺失值
df_2.fillna(df_2.max())

#用每列中最小值填补每列中的NA缺失值
df_2.fillna(df_2.min())

#用每列中均值填补每列中的NA缺失值
df_2.fillna(df_2.mean())

#按行的缺失删除
df_2.dropna(axis = 0)

#按列的缺失删除
df_2.dropna(axis = 1)

#将省份中“湖北”换成“鄂”
df_2.replace('湖北','鄂')

#只取省份这一列，将省份中“湖北”换成“鄂”
df_2['City'].replace('湖北','鄂')

#将湖北、北京、上海均替换成其对应的省份简称
df_2.replace({'湖北':'鄂','北京':'京','上海':'沪'})

#按照一定的顺序排列其行和列
df_2.reindex([0,9,6,1,5,7,4,8,2,3],['Name','Age','Salary','Salary','Id'])