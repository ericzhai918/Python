#删除字符串中不需要的字符

s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

#中间有空格
s = ' hello    world \n'
s = s.strip()
print(s)

#replace()
print(s.replace('   ',''))

#re
import re
print(re.sub('\s+',' ',s))

#应用
# with open(filename) as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)