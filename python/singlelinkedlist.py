class node:
    def __init__(self,info):
        self.info=info
        self.link=None
start=None
count=0
def add_beg(data):
    global start
    temp=node(data)
    if start==None:
        start=temp
        
    else:

        temp.link=start
        start=temp
def add_end(data):
    global start
    temp=node(data)
    if(start==None):
        add_beg(data)
    else:
        p=start
        
        while(p.link!=None):
            p=p.link
        p.link=temp
def add_at_postion(pos,data):
    count1=0
    if start==None:
        add_beg(data)
    else:
        temp=node(data)
        p=start
        prev=None
        while p.link!=None :
            if(pos==count1):
                temp.link=p
                prev.link=temp
                break
            else:
                prev=p
                p=p.link
                count1+=1
def del_at_beg():
    global start
    if(start==None):
        print("empty list")
    else:
        p=start
        if(p.link==None):
            del p
        else:
            start=p.link
            del p
def del_at_end():
    global start
    if(start==None):
        print("empty list")
    else:
        p=start
        while p.link!=None:
            prev=p
            p=p.link
        prev.link=None

def del_at_postion(pos):
    global start
    p=start
    count1=0
    if(start==None):
        print("empty list")
    else:
        while(p.link!=None):
            if (pos==count1):
                prev.link=p.link
                p.link=None
                break
            else:
                prev=p
                p=p.link
                count1+=1

def display():
    if(start==None):
        print("empty list ")
    else:
        p=start
        while p!=None:
            print(p.info)
            p=p.link
def rev_linkedList():
    global start

    prev=None
    current=start
    if start==None:
        print("list is empty")
    else :
        while(current!=None):
            next=current.link
            current.link=prev
            prev=current
            current=next
    start=prev
    display()
     
while(True):
    print("\t\t 1.add node at beg")
    print("\t\t 2.add node at end")
    print("\t\t 3.display")
    print("\t\t 4.add at pos")
    print("\t\t 5.add at middle")
    print("\t\t 6.del at beg")
    print("\t\t 7.del at end")
    print("\t\t 8.del at pos")
    print("\t\t 9.del at middle")
    print("\t\t 10.reverse the list")

    print("\t\t 0.exit")
    choice=int(input())
    if choice==1:
        data = int(input("enter the data "))
        count+=1
        add_beg(data)
    elif choice==2:
        data = int(input("enter the data "))
        count+=1
        add_end(data)
    elif choice==3:
        display()
    elif choice==4:
        
        pos=int(input("enter the pos to add "))
        if pos>=count:
            print("invalid position")
        else:
            data = int(input("enter the data "))
            add_at_postion(pos,data)
            count+=1
    elif choice == 5:
        pos=int(count/2)
        data = int(input("enter the data "))
        add_at_postion(pos,data)
        count+=1
    elif choice==6:
        del_at_beg()
        count-=1
    elif choice==7:
        del_at_end()
        count-=1
    elif choice==8:
        pos=int(input("enter the pos to add "))
        if pos>=count:
            print("invalid position")
        else:
            del_at_postion(pos)
            count-=1
    elif choice == 9:
        pos=int(count/2) 
        del_at_postion(pos)
        count-=1
    elif choice ==10:
        rev_linkedList()
    elif choice==0:
        break
    
    else:
        print("invalid selection ")
print(count)