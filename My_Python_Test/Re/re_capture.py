import re
str1 = "123@qq.comaaa@163.combbb@126.comasdf111@asdfcom"
a = re.findall(r'\w+@(qq|163|126)\.com',str1)
print(a)
b = re.findall(r'\w+@(?:qq|163|126)\.com',str1)
print(b)
