a = list(range(1, 11))
print(a)

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

b = [x * x for x in range(1, 11)]
print(b)

c = [x*x for x in range(1,11) if x % 2 ==0]
print(c)

d = [m+n for m in 'ABC' for n in "XYZ"]
print(d)

e = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in e.items():
    print(k,'=',v)

print([k+'='+v for k,v in e.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])