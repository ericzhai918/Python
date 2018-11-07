#BytesIO实现了在内存中读写bytes

#创建一个BytesIO写入bytes
from io import BytesIO
f=BytesIO()

print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

#在BytesIO读bytes
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
print(f.read().decode('utf-8'))