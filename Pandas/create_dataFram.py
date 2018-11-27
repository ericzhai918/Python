import pandas as pd
import numpy as np

# 空的 DataFrame
df = pd.DataFrame()
print(df)

# ndarrays 创建 DataFrame
data = {'Name': ['A', 'B', 'C', 'D'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['row_1', 'row_2', 'row_3', 'row_4'])
print(df)

# List 创建 DataFrame
list_data = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(list_data, columns=['col_1', 'col_2', 'col_3'], index=['row_1', 'row_2'])
print(df)

# series 创建 DataFrame
series_data = {'col_1': pd.Series([5, 7, 9], index=['row_1', 'row_2', 'row_3']),
               'col_2': pd.Series([1, 2, 3, 4], index=['row_1', 'row_2', 'row_3', 'row_4'])}
df = pd.DataFrame(series_data)
print(df)
