
#关键字参数什么都能传，这点我很不爽，要限制它传进去的东西怎么办？
#命名关键字参数,以*分隔

def person(name,age,*,city,job):
    print(name,age,city,job)

person('Jack',24,city='Shanghai',job="OA")
person('Jack',24,job="OA",city='Shanghai')

#有可变参数，省略*
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

person('Jack',24,'Beijing','Engineer')#报错

#命名关键字参数可以有缺省值
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)

person('Jack',24,job='Engineer')