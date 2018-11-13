from functools import reduce


def fn(x, y):
    return x * 10 + y


r1 = reduce(fn, [1, 2, 3, 4, 5])
print(r1)

r2 = reduce(lambda x, y: x * 10 + y, [1, 2, 3, 4, 5])
print(r2)
