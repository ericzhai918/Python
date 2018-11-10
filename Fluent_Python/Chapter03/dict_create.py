a = dict(one=1, two=2, three=3)
print(a)

b = {'one': 1, 'two': 2, 'three': 3}
print(b)

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)

d = dict([('two', 2), ('three', 3), ('one', 1)])
print(d)

e = dict({'one': 1, 'two': 2, 'three': 3})
print(e)

print(a == b == c == d == e)