from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)
print(dict(c))
print(c['x'])
print(c['y'])
print(c['z'])

