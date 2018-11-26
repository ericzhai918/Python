import re

pattern = re.compile(r'\d+')
r1 = pattern.findall('runoob 123 google 456')
r2 = pattern.findall('run88oob123google456', 0, 10)

print(r1)
print(r2)
