import re

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)

m1 = pattern.match('one12twothree34four', 2, 10)
print(m1)

m2 = pattern.match('one12twothree34four', 3, 10)
print(m2)

print(m2.group())
print(m2.group(0))

print(m2.start())
print(m2.end())
print(m2.span())

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# span([group]) 方法返回 (start(group), end(group))。
