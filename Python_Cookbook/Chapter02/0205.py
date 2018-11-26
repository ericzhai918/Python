# 字符串搜索和替换

# 使用 str.repalce() 方法
text = 'yeah, but no, but yeah, but no, but yeah'
a = text.replace('yeah', 'yep')
print(a)

# 使用re.sub()函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

b = re.sub(r'(\d+)+/(\d+)+/(\d+)+', r'\3-\1-\2', text)
print(b)

# 先编译后替换
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# 传递一个替换回调函数
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


a = datepat.sub(change_date, text)
print(a)

# 打出替换次数
newText, n = datepat.subn(r'\3-\1-\2', text)
print(n)
print(newText)
