# 使用 itemgetter 排序一个元组列表

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
#会排序
from operator import itemgetter
for city in sorted(metro_data,key=itemgetter(1)):
    print(city)

#不会排序
cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))
