#prime numbers in a range
import copy
def checkprime(a):
    k=a/2
    i=2
    while(i<=k):
        if a%i==0: 
            return 0
        i+=1
    return 1
firstnum,secondnum=list(map(int,input("enter the 2 numbers ").split(" ")))
a=firstnum
while(a<=secondnum):
    if checkprime(a):
        print(a)
    a+=1

 #Count the total number of digits in a number

mylist=[2,3,4,5,7,7,8,89,9,0,0]
lenght_of_list=0
copy_list=mylist.copy()
while(mylist):
    mylist.pop()
    lenght_of_list+=1
print(copy_list)
print("lenght of an list is ",lenght_of_list)

#Print list in reverse order using a loop

mylist=[2,3,4,5,7,7,8,89,9,0,0]
lenght_of_list=0
copy_list=list()
while(mylist):
    k=mylist.pop()
    copy_list.append(k)
print("printing the list in reverse order",copy_list)
