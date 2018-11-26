#字符串开头或结尾匹配

filename = 'spam.txt'
end = filename.endswith('.txt')
print(end)
start = filename.startswith('file:')
print(start)

url = 'http://www.python.org'
start = url.startswith('http:')
print(start)

#检查多种匹配可能
import os
filenames = os.listdir('.')
print(filenames)

x = [name for name in filenames if name.endswith(('.c','.h','.py'))]
print(x)

a = any(name.endswith('py') for name in filenames)
print(a)

#
from urllib.request import urlopen

def read_data(name):
    if name.startswith('http:','https:','ftp:'):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:','ftp:']
url = "http://www.python.org"
start = url.startswith(tuple(choices))
print(start)