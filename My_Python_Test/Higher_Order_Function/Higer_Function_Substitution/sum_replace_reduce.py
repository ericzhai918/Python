#计算 0-99 之和
from functools import reduce
from operator import add

a = reduce(add, range(100))
print(a)
b = sum(range(100))
print(b)
