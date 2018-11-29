import pandas as pd
import numpy as np
########################可视化########################

#线图
df = pd.DataFrame(np.random.randn(20,3),index=np.linspace(0,19,20), columns=list('ABC'))
df.plot()

#条形图
df = pd.DataFrame(np.random.randn(5,3)+10,index=np.linspace(0,4,5), columns=list('ABC'))
df.plot.bar()

#直方图
df = pd.DataFrame({'A':np.random.randn(100),'B':np.random.randn(100)+1,'C':np.random.randn(100)+2})
df.hist(bins=20)

#箱线图
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()

#散点图
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')

#饼图
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)