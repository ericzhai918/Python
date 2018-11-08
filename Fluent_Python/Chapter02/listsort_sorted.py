fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))

print(fruits)

print(sorted(fruits,reverse=True))

print(sorted(fruits,key=len))
#长度一样时， grape 和 apple的相对位置不会改变
print(sorted(fruits,key=len,reverse=True))

print(fruits)

print(fruits.sort())
