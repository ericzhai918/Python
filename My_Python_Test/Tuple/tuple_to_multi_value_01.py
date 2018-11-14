# 解压序列赋值给多个变量
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACE', 50, 45.3, (2012, 20, 12)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(year)
print(day)

# 这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组

s = 'Hello'
a, b, c, d, e = s
print(a)
print(e)

# 只想解压一部分

data = ['Ace', 50, 91.1, (2018, 10, 26)]
_, shares, price, _ = data
print(price)
