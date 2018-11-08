# 用*运算符把一个可迭代对象拆开作为函数的参数
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient)
print(remainder)