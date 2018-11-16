# 使用 reduce 函数和一个匿名函数计算阶乘
from functools import reduce

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

print(fact(4))


# operator模块为多个算术运算符提供了对应的函数,从而避免编写lambda a, b: a*b 这种平凡的匿名函数

from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul,range(1,n+1))

print(fact(4))

