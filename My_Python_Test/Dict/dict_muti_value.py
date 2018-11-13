from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print(e)

# 比较
pairs = {'A':1,'B':4,'C':[3, 4]}
d = {}
for key, value in pairs.items():
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

#哈
d =defaultdict(list)
for key,value in pairs.items():
    d[key].append(value)
print(d)
