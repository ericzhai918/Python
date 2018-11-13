from functools import reduce


def add(x, y):
    return x + y


r1 = reduce(add, [1, 2, 3, 4, 5])
print(r1)

r2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(r2)