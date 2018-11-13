#根据单词长度给一个列表排序
fruits = ['strawberry','fig','apple','cherry','raspberry','banana']

a = sorted(fruits,key=len)
print(a)

#根据反向拼写给一个单词列表排序
def reverse(word):
    return word[::-1]

b = sorted(fruits,key=reverse)
print(b)