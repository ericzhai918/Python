
#使用生成器表达式计算笛卡儿积
colors = ['black','white']
sizes = ['S','M','L']
for tshirt in ('%s %s'%(c,s) for c in colors for s in sizes):
    print(tshirt)

#生成器逐个产出元素,生成器表达式会在每次 for 循环运行时才生成一个组合
#如果要计算两个各有 1000 个元素的列表的笛卡儿积
# 生成器表达式就可以帮忙省掉运行 for 循环的开销