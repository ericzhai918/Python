
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)

#字符串也是可迭代对象
for ch in 'ABC':
    print(ch)

#判断是否为可迭代类型
from collections import Iterable
a=isinstance('abc',Iterable)
print(a)

b=isinstance([1,2,3],Iterable)
print(b)

c= isinstance(123,Iterable)
print(c)


#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)