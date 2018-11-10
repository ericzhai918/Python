# 迭代字典的key
d = {'A': 1, 'B': 2, 'C': 3}
# 默认迭代key
for key in d:
    print(key)

# 如果强行迭代value，会报错
# for key,value in d:
#     print(key,value)

# 迭代字典的key，value
for key, value in d.items():
    print(key, value)

# 迭代字典的key
for key in d.keys():
    print(key)

# 迭代字典的value
for value in d.values():
    print(value)

# 迭代两个变量
for x, y in [(1, 1,), (2, 4), (3, 9)]:
    print(x, y)

# 字符串迭代
for x in "ABC":
    print(x)

#如果我想为迭代元素加上序号呢？
for i ,x in enumerate(['A','B','C']):
    print(i,x)

# 判断是否为可迭代对象
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance({"A": 1, "B": 2}, Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance(123, Iterable))
