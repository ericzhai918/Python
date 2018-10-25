# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

sum = 0
print("无重复数字的三位数如下:")
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)
                sum = sum + 1
print("能组成%s个互不相同且无重复数字的三位数"%(sum))
