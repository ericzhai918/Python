import pandas as pd

# df_2 = pd.read_csv('Salary_2.txt', sep=',', header='infer', encoding='utf-8')
# df_1 = pd.read_csv('Salary1.txt', sep=',', header='infer', encoding='utf-8')

# # 按列合并
# pd.concat([df_1, df_2], axis=1)
# # 按行合并
# pd.concat([df_1, df_2], axis=0)

##################################merge

left_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5'],
})

right_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})

print(left_data)
print('===========================================')
print(right_data)

# 按id合并两个数据集（此时how是默认值：内连接）
print(pd.merge(left_data, right_data, on='id'))

#按subject_id合并两个数据集,左连接方式
print(pd.merge(left_data,right_data,on='subject_id',how='left'))

#按subject_id合并两个数据集,右连接方式
print(pd.merge(left_data,right_data,on='subject_id',how='right'))