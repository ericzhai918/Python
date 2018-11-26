# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none

import re

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) (.*)', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.group(3) : ", matchObj.group(3))
else:
    print('No match!')
