#memoryview内存视图
#用户在不复制内容的情况下操作同一个数组的不同切片
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
mem = memoryview(numbers)
print(len(mem))

print(mem[0])

mem_oct = mem.cast('B')
print(mem_oct.tolist())

mem_oct[5] = 4

print(numbers)
