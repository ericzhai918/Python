
# 星号用在字符串的分割

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# 解压元素后丢弃
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
