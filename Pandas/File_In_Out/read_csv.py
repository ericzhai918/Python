import pandas as pd

filename = 'Salary.txt'
df = pd.read_csv('Salary.txt', sep=',', header='infer', encoding='utf-8')
df.to_csv('Salary1.txt',sep='\t',header='infer',encoding='utf-8',index=False)

