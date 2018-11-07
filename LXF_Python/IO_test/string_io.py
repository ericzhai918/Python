#StringIO顾名思义就是在内存中读写str

#把str写入StringIO
from io import StringIO
f = StringIO()

print(f.write('Hello'))
print(f.write(''))
print(f.write("Hello Alex&Lisa"))
print(f.getvalue())

#读取StringIO

from io import StringIO

f = StringIO('Hello!\nHi\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())