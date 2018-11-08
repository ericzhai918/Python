#具名元组的属性和方法
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
# _fields 属性是一个包含这个类所有字段名称的元组
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi1 = City(*delhi_data)

#_make()通过接受一个可迭代对象来生成这个类的一个实例跟 City(*delhi_data) 是一样的
print(delhi)
print(delhi1)

# _asdict() 把具名元组以 collections.OrderedDict 的形式返回
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)