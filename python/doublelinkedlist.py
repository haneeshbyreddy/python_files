class doublenode:
    def __init__(self,info):
        self.info=info
        self.prev=None
        self.next=None
start = None
count=0
def add_beg(data):
    global start
    temp=doublenode(data)
    if start==None:
        start=temp
    else:
        temp.next=start
        start.prev=temp
        start=temp
def add_end(data):
    global start
    temp=doublenode(data)
    pv=start
    while(pv.next!=None):
        pv=pv.next
    temp.prev=pv
    pv.next=temp
def add_pos(data,pos):
    global start
    count1=0
    temp=doublenode(data)
    if start== None:
        print("empty node")
    else:
        pv=start
        current=None
        while(pv!=None):
            if(count1==pos):
                temp.prev=current
                current.next=temp
                temp.next=pv
                pv.prev=temp
                break
            else:
                current=pv
                pv=pv.next
                count1+=1
def del_at_beg():
    global start
    if start==None:
        print("empty list canot delete")
    else: 
        pv=start
        b=pv.next
        b.prev=None
        start.next=None
        start=b
def del_at_end():
    global start
    if start==None:
        print("empty list canot delete")
    else:
        p=start
        while(p.next!=None):
            back=p
            p=p.next
        back.next=None
        del p
def del_at_pos(pos):
    global start
    p=start
    b=None
    count1=0
    if(start==None):
        print("empty")
    else:
        while(p!=None):
            if(pos==count1):
                t=p.next
                b.next=t
                p.next=None
                
                break
            else:
                b=p
                p=p.next
                count1=count1+1
def reverse_display():
    global start
    if(start == None):
        print("list is empty")
    else:
        
        current = start
        while(current.next!=None):
            front = current.next
            back = current.prev
            current.prev = front
            current.next = back
            current = current.prev
        start = current.prev
        print("reversed linked list is:")
        print(current.info)
        display()
def display():
    global start
    if start==None:
        print("empty node")
    else:
        pv=start
        while(pv.next!=None):
            print(pv.info)
            pv=pv.next
        print(pv.info)

while(True):
    print("\t\t 1.add node at beg")
    print("\t\t 2.display")
    print("\t\t 3.add at end")
    print('\t\t 4.add at position')
    print("\t\t 5.add at middle")
    print("\t\t 6.delete at beg")
    print("\t\t 7.del at end")
    print("\t\t 8.del at pos")
    print("\t\t 9.del at middle")
    print("\t\t 10.reverse the")
    print("\t\t 0.exit")
    choice=int(input())
    if choice==1:
        data = int(input("enter the data "))
        count+=1
        add_beg(data)
    elif choice==2:
        display()
    elif choice == 3:
        data = int(input("enter the data "))
        count+=1
        add_end(data)
    elif choice== 4:
        pos=int(input("enter the position to add "))
        data = int(input("enter the data "))
        count+=1
        
        add_pos(data,pos)
    elif choice== 5:
        pos=int(count/2)
        data = int(input("enter the data "))
        add_pos(data,pos)
        count+=1
    elif choice==6:
        del_at_beg()
        count=count-1
    elif choice==7:
        del_at_end()
        count=count-1
    elif choice==8:
        pos = int(input("enter the pos"))
        del_at_pos(pos)
        count=count-1
    elif choice==9:
        pos=int(count/2)
        del_at_pos(pos)
        count=count-1
    elif choice==10:
        reverse_display()
    elif choice==0:
        break
        