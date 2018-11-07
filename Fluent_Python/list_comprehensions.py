#把一个字符串变成 Unicode 码位的列表
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

#使用列表推导
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(type(codes))
print(codes)

#列表推导使用原则：只用列表推导来创建新的列表，并且尽量保持简短。
#如果列表推导的代码超过了两行，你可能就要考虑是不是得用 for 循环重写了


#推导不会出现变量泄漏
x ='ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)
#表达式内部的变量和赋值只在局部起作用。


#3种不同尺寸的T恤衫，每个尺寸都有2个颜色，用列表推导算出了这个列表
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)