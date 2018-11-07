
#你回发现原来的文件内容被覆盖了
f = open('E:\\Python\\LXF_Python\\IO_test\\test.txt','w')
f.write("HELLO ZHAI")
f.close()

#模式选用a+，在文件后追加
f = open('E:\\Python\\LXF_Python\\IO_test\\test.txt','a+')
f.write("HELLO ZHAI")
f.close()