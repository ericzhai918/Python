import pandas as pd

df1 = pd.read_csv('1.txt',sep=' ',header='infer', encoding='GBK',error_bad_lines=False)
df3 = pd.read_csv('3.txt',sep='\t',header='infer', encoding='GBK',error_bad_lines=False)
df2 = pd.read_csv('2.txt',sep=' ',header='infer', encoding='GBK',error_bad_lines=False)


print(pd.merge(df2, df1, on='虚机IP'))

