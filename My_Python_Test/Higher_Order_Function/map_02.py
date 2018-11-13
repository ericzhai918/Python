def f(x):
    return x * x


l = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    l.append(f(n))
print(l)

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

s = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(s))
