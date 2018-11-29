import pandas as pd
import numpy as np
from numpy.random import randn

#########################数据显示########################

# DataFrame 是由多个 Series 组成的
df = pd.DataFrame(data=randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
# DataFrame, 是由 4 个长度为 5 的 Series 组成的
print(df)

print(df['W'])
# 证明DataFrame由Series 组成
print(type(df['W']))

# 取指定列
print(df[['W', 'Y']])

# 取指定行
# 使用loc
print(df.loc[['A', 'B']])

# 使用iloc
print(df.iloc[[0, 1]])

# 条件查找
print(df['W'] > 0)
print(df[df['W'] > 0])
print(df[(df['W'] > 0) & (df['Y'] < 0)])
print(df[(df['W'] > 0) & (df['Y'] < 0)]['W'])

# 信息展示
long_df = pd.DataFrame(data=randn(500, 4), columns=['W', 'X', 'Y', 'Z'])
print(long_df.head())
print(long_df.tail())
# 打印出 DataFrame 中所有的统计信息
print(long_df.describe())

# DataFrame 的数据修改

# 新建列
df = pd.DataFrame(data=randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
df['666'] = df['W'] + df['X']
print(df)

# 删除列,指定axis=1,若改变自身inplace=True
df.drop('W', axis=1, inplace=True)
print(df)

# 增加行
df.loc['Z'] = [1, 2, 3, 4]
print(df)

# 删除行,指定axis=0,若改变自身inplace=True
df.drop('B', axis=0, inplace=True)
print(df)

############################数据连接########################

# 按行合并
df1 = pd.DataFrame(data=randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
df2 = pd.DataFrame(data=randn(5, 4), index=['F', 'G', 'H', 'I', 'J'], columns=['W', 'X', 'Y', 'Z'])
print(pd.concat([df1, df2]))

# 按列合并
df1 = pd.DataFrame(data=randn(5, 2), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X'])
print(df1)
print('-' * 10)
df2 = pd.DataFrame(data=randn(5, 3) * 10, index=['F', 'G', 'H', 'I', 'J'], columns=['W', 'X', 'Y'])
print(df2)
print('-' * 10 + '\n concat')
print(pd.concat([df1, df2], axis=1))

# Merge 合并

df1 = pd.DataFrame(data=randn(5, 2), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X'])
print(df1)
print('-' * 10)

df2 = pd.DataFrame(data=randn(5, 1) * 10, index=['A', 'B', 'C', 'D', 'E'], columns=['Z'])
df2['X'] = df1['X']
print(df2)

print('-' * 10 + '\n merge')
print(pd.merge(df1, df2, on='X'))

# how: 包括'left', 'right', 'outer' , 'inner'分别是左连接，右连接，外连接与内连接，其逻辑与数据库的连接是相同的
# on: 连接所基于的关键字（列），比如上个例子的 on 就是'X'，如果 on 为空，那么默认 on 为两个 DataFrame 中所有同名列

########################数据操作########################
df = pd.DataFrame(data=randn(5, 2), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X'])
df['Name'] = ['Bob', 'Jony', 'Bob', 'Alice', 'Bob']
print(df)
# 统计数据集中‘Name’的种类与个数
print(df['Name'].unique())
print(df['Name'].nunique())
print(df['Name'].value_counts())


# 批量运算

# 将df W 列的值乘两倍
def double_it(x):
    return x * x
print(df['W'].apply(double_it))
print(df['W'].apply(lambda x: x * x))

#数据补全
df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
df['x'].loc['b'] = np.NaN
print(df)

#查看是否有缺失值
print(df.isna().sum())

#填补缺失值
df.fillna(df.median(),inplace=True)
print(df)

#分组统计
df = pd.DataFrame(data=np.round(randn(8,1)*1000+3000),columns=['Salary'])
df['Name'] = ['Bob','Jony','Bob','Alice','Bob','Jony','Jony','Alice']
print(df)

#查找每个人的总薪水groupby
print(df.groupby('Name').sum())

#正序
print(df.groupby('Name').sum().sort_values(by='Salary'))

#倒序
print(df.groupby('Name').sum().sort_values(by='Salary',ascending=False))


