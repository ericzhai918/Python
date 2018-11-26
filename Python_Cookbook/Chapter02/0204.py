# 字符串匹配和搜索

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))

#
import re
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# 使用同一个模式去做多次匹配
datapat = re.compile(r'\d+/\d+/\d+')
if datapat.match(text1):
    print('Y')
else:
    print('N')
if datapat.match(text2):
    print('Y')
else:
    print('N')

# findall() 查找字符串任意部分的模式出现位置
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
a = datapat.findall(text)
print(a)

#
datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datapat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
a = datapat.findall(text)
print(a)
for month, day, year in datapat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

#
for m in datapat.finditer(text):
    print(m.groups())



