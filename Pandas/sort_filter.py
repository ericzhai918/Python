import pandas as pd

df_2 = pd.read_csv('Salary_2.txt', sep=',', header='infer',encoding = 'utf-8')

#筛选符合特定条件的行
df_2[df_2.Age > 25]

#用&符号实现多条件的选择,同时选择年龄大于25且薪资高于9000的数据
df_2[(df_2.Age > 25) & (df_2.Salary>9000)]

#用|符号实现多条件“或”的选择，大于25岁或者薪资大于9000
df_2[(df_2.Age > 25) | (df_2.Salary>9000)]

#按“年龄”升序照列
df_2.sort_values(by='Age',ascending=True)

#先按列Age升序排列，后按Id降序排列数据
df_2.sort_values(['Age','Id'], ascending=[True,False])