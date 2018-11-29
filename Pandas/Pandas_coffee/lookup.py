#数据信息查看/描述统计
import pandas as pd

df = pd.read_csv('Salary.txt', sep=',', header='infer', encoding='utf-8')
print(df)
print(df.head(5))#查看DataFrame前5行
print(df.tail(5))#查看DataFrame后5行
print(df.size)#查看DataFrame总元素个数
print(df.values)#查看DataFrame数据，以array返回
print(df['Name'].values)#查看DataFrame某列（例如Name），以array返回
print(df.index)#查看DataFrame索引
print(df.columns)#查看DataFrame列

print(df['Age'].count())
print(df['Age'].max())#所有值中的最大值
print(df['Age'].min())#所有值中的最小值
print(df['Age'].mean())#所有值的平均值
print(df['Age'].median())#所有值的中位数
print(df['Age'].sum())#所有值之和
print(df['Age'].std())#值的标准偏差
print(df['Age'].abs())#绝对值
print(df['Age'].value_counts())#查看这一列的值统计
print(df['Age'].unique())#取唯一值

