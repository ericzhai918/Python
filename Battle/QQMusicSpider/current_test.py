from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import datetime

#线程的执行方法
def print_value(value):
    print("Thread"+str(value))

#每个进程里面的线程
def myThread(value):
    #ThreadPoolExecutor线程池
    Thread = ThreadPoolExecutor(max_workers=2)
    Thread.submit(print_value,datetime.datetime.now())
    Thread.submit(print_value,datetime.datetime.now())

def myProcess():
    #ProcessPoolExecutor进程池
    pool = ProcessPoolExecutor(max_workers=2)
    pool.submit(myThread,datetime.datetime.now())
    pool.submit(myThread,datetime.datetime.now())

if __name__=='__main__':
    myProcess()
