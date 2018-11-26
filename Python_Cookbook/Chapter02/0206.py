#字符串忽略大小写的搜索替换
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
a = re.findall('python',text,flags=re.I)
print(a)

b = re.sub('python','snake',text,flags=re.I)
print(b)

#
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

a = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(a)