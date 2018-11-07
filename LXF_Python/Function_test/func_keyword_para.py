
def person(name, age, **kw):
    print('name:', name, 'age:', age, '', 'other:', kw)

#仅传入必选参数
person("Lisa",18)
#传入任意个数的关键字参数
person('Alex',22,city="Shanghai")
person('Adam',45,gender="M",job='OA')
#**extra会自动解包为dict
extra = {'city':'Beijing','job:':'OA'}
person('Cooper','M',**extra)