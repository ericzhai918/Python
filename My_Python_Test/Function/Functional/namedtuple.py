from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.23423, 139.1234))
print(tokyo)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)
LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(delhi_data)
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ":", value)
