#把一个对象序列化并写入文件
import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

#把对象从磁盘读到内存
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
