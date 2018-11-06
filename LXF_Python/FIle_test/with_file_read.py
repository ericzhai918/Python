
#文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用
# f = open('E:\\Python\\LXF_Python\\FIle_test\\test.txt','r')
# print(f.read())
# f.close()

#保证无论是否出错都能正确地关闭文件
# try:
#     f = open('E:\\Python\\LXF_Python\\FIle_test\\test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#为了简洁代码，使用with代替try ... finally
# with open('E:\\Python\\LXF_Python\\FIle_test\\test.txt', 'r') as f:
#     print(f.read(),'第一次调用')

#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了
#我们用readline()一行一行的读
# with open('E:\\Python\\LXF_Python\\FIle_test\\test.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         print(line)
#         line = f.readline()
#     f.close()
