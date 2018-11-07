#我们经常计算x的平方，可以使用默认参数
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5,3))

#一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

print('Lisa', 'F')
print('Alex', 'M')


#继续传入年龄、城市。由于入学年龄，入学城市大都相同，设为默认
def enroll(name, gender, age=6, city="Shanghai"):
    print('name:', name)
    print('gender:', gender)
    print('age', age)
    print('city', city)

enroll('Lisa','F')
enroll('Alex','M',7)
enroll('Adam','M',city='Tianjin')

#注意：默认函数的坑。默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,2,3]))
print(add_end(['b','c','a']))

print(add_end())
print(add_end())
print(add_end())

#跳过大坑，使用不可变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())
