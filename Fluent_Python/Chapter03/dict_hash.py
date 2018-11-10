t = (1, 2, (30, 40))
print(hash(t))
t1 = (1, 2, [30, 40])
print(hash(t1))#报错
t2 = (1, 2, frozenset([30, 40]))
print(hash(t2))

print(hash('Lisa'))

print(hash(18))

b = bytes(10)
print(hash(b))
