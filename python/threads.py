from threading import *
'''num1=0
l=Lock()
def thread(num):
    global num1
    l.acquire()
    for i in range(1,num+1):
        
        print("thread ",i," is executing")

        num1+=i
    l.release()
    print(num1)
n=10
t=Thread(target=thread,args=(n,))
t1=Thread(target=thread,args=(n,))
t.start()
t1.start()
'''
from threading import *
l=Semaphore(2)
num1=0
def thread(num):
    global num1
    l.acquire()
    for i in range(1,num+1):
        
        print("thread ",i," is executing")

        num1+=i
    l.release()
    print(num1)
n=10
t=Thread(target=thread,args=(n,))
t1=Thread(target=thread,args=(n,))
t2=Thread(target=thread,args=(n,))
t3=Thread(target=thread,args=(n,))
t.start()
t1.start()
t2.start()
t3.start()
