a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# 找到相同的键
c = {key: a[key] for key in a.keys() & b.keys()}
print(c)

# 找到相同的键:值
d = {item for item in a.items() & b.items()}
print(d)

# a中有的，b中没有的键
e = {key: a[key] for key in a.keys() - b.keys()}
print(e)
