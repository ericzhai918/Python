#deque双向队列
from collections import deque

queue = deque(['A','B','C','D'])
#从尾部插入元素
queue.append("E")
print(queue)

#从头部插入元素
queue.appendleft("X")
print(queue)

#查找某个元素的索引位置
print(queue.index('A'))

#在指定位置插入元素
queue.insert(1,'Z')
print(queue)

#反转
queue.reverse()
print(queue)

#获取最右边一个元素，并在队列中删除
# print(queue.pop())
# print(queue)

#获取最左边一个元素，并在队列中删除
# print(queue.popleft())
# print(queue)

#删除指定元素
queue.remove('A')
print(queue)

#从队列右边扩展一个列表的元素
queue.extend([1,2])
print(queue)

#从队列左边扩展一个列表的元素
queue.extendleft([3,4])
print(queue)

#把右边元素放到左边
queue.rotate(2)
print(queue)

#浅拷贝
new_queue = queue.copy()
print(new_queue)

#清空队列
new_queue.clear()
print(new_queue)

#限制deque的长度,之前的顶出去
a = deque(maxlen=3)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
print(a)