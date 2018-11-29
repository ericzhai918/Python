import pandas as pd
import numpy as np

# 通过数组创建Series
data = [10, 20, 30]
print(pd.Series(data))

# 为 Series 设置索引
labels = ['a', 'b', 'c']
data = [10, 20, 30]
print(pd.Series(data=data, index=labels))

# 通过 np.array 或者字典对象创建Series
labels = ['a', 'b', 'c']
data = [10, 20, 30]
arr = np.array(data)
d = {'a': 10, 'b': 20, 'c': 30}

# 通过数组创建
a = pd.Series(data=data, index=labels)
print(a)

# 通过np.array创建
b = pd.Series(data=arr, index=labels)
print(b)

# 通过字典创建，key作为索引，value作为数据值
c = pd.Series(data=d)
print(c)

# Series可以用于存储任何对象
d = pd.Series(data=[print, len, dict], index=['a', 'b', 'c'])
print(d)

# 两个 Series 的数值四则运算
ser1 = pd.Series([1, 2, 3], ['a', 'b', 'c'])
ser2 = pd.Series([1, 0, 1], ['a', 'c', 'd'])
print(ser1)
print(ser2)
print(ser1/ser2)
