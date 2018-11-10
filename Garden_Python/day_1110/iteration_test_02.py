# 迭代器是一个可以记住遍历的位置的对象
# iter() next() 只进不退

#next()每次遍历下一个
# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))

# 使用for遍历list的每一个元素
# list = [1, 2, 3, 4]
# it = iter(list)
# for x in it:
#     print(x)

#使用next()函数遍历list的每一个元素
import sys
list = [1,2,3,4]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

#创建一个迭代器（讲过面向对象再写）