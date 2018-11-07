
#切片练习一
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n =3
for i in range(n):
    r.append(L[i])

print(r)
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

#练习二
L = list(range(100))
print(L)
print(L[:10])#前10个数
print(L[-10:])#后10个数
print(L[10:20])#前11-20个数
print(L[:10:2])
print(L[::5])
print(L[:])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作
print((0,1,2,3,4,5,6,7)[:3])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符
print('ABCDEFGH'[:2])