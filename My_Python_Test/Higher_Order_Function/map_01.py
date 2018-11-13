def square(x):
    return x ** 2


m1 = map(square, [1, 2, 3, 4, 5])
print(m1)
print(list(m1))

m2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(m2)
print(list(m2))

m3 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(m3))
