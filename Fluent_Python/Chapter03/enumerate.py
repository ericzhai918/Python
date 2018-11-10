# 使用enumerate
season = ['Spring', 'Summer', 'Auturm', 'Winter']
e = enumerate(season)
print(list(e))

d = enumerate(season, start=1)
print(list(d))

# 普通的for循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

# for循环使用enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, seq[i])
