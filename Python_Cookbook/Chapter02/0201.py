#使用多个界定符分割字符串
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'

a = re.split(r'[;,\s]\s*', line)
print(a)

#捕获分组
b = re.split(r'(;|,|\s)\s*',line)
print(b)

values = b[::2]
print(values)

delimiters = b[1::2]+['']
print(delimiters)

c = ''.join(v+d for v,d in zip(values,delimiters))
print(c)

#非捕获字符?:
d = re.split(r'(?:;|,|\s)\s*',line)
print(d)