# 最短匹配模式
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
a = str_pat.findall(text1)
print(a)

text2 = 'Computer says "no." Phone says "yes."'
b = str_pat.findall(text2)
print(b)

str_pat = re.compile(r'\"(.*?)\"')
c = str_pat.findall(text2)
print(c)
