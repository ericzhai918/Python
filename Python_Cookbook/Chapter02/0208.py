# 多行匹配模式
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
        multiline comment */
        '''
a = comment.findall(text1)
b = comment.findall(text2)

print(a)
print(b)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
c = comment.findall(text2)
print(c)