
import os
print(os.name)# 操作系统类型
print(os.environ)#环境变量
print(os.environ.get('PATH'))#某个环境变量的值

print(os.path.abspath('.'))# 查看当前目录的绝对路径
print(os.path.join('E:\\','testDirS'))# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('E:\\testDirS')# 然后创建一个目录
os.rmdir('E:\\testDirS')# 删掉一个目录

print(os.path.split('E:\\testDirS'))
print(os.path.splitext('E:\\testDirS'))

print(os.rename('test.txt', 'test.py'))# 对文件重命名
print(os.remove('test.py'))# 删掉文件

#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

#列出所有的.py文件
os.chdir('E:\\Python\\LXF_Python\\Function_test')
print([x for x in os.listdir('E:\\Python\\LXF_Python\\Function_test') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

os.chdir('E:\\Python\\LXF_Python\\Function_test')
for x in os.listdir('E:\\Python\\LXF_Python\\Function_test'):
    t=os.path.splitext(x)
    if os.path.isfile(x) and t[1] == '.py':
        print(x)