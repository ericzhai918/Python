# 计算阶乘
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

# 使用map()
a = list(map(fact, range(6)))
print(a)

# 使用列表推导式
b = [fact(n) for n in range(6)]
print(b)

# 使用filter()
x = list(map(factorial, filter(lambda n: n % 2, range(6))))
print(x)

# 使用列表推导式
y = [factorial(n) for n in range(6) if n % 2]
print(y)


