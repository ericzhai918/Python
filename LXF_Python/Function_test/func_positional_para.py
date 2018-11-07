# 计算x的平方
def power(x):
    return x * x

print(power(2))


# 如果要计算x的三次方，四次方呢?x*x*x,x*x*x*x这样显然很冗余
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,2))
print(power(5,3))


