'''#import pdb
#breakpoint()
class node:
    def __init__(self,info):
        self.info = info
        self.link = None
start = None
count = 0

def add_at_beg(data):
    global start
    temp = node(data)
    if(start == None):
        start = temp
    else:
        temp.link = start
        start = temp

def add_at_end(data):
    global start
    temp = node(data)
    if(start == None):
        start = temp
    else:
        p = start
        while p.link!=None:
            p=p.link
        p.link = temp
        
def add_at_middle(data):
    global start
    temp = node(data)
    if(start == None):
    	start = temp
    else:
    	p = start
    	prev = None
    	while(data>=p.info):
    		prev = p
    		p=p.link
    	temp.link = p
    	prev.link = temp

def add_at_position(data,pos):
	global start
	global count
	temp = node(data)
	if(start == None):
		start = temp 
	else:
		p = start
		prev = None
		while(p.link!=None):
			#print(count)
			if(pos == count):
				temp.link = p
				prev.link = temp
				count = 0
				break
			else:
				prev = p
				p = p.link 
				count=count+1

def del_at_beg():
	global start
	if(start == None):
		print("list is empty to delete")
	else:
		p = start
		p = None
		start = start.link
		
		
def del_at_end():
	global start
	if(start == None):
		print("list is empty to delete")
	else:
		p = start
		while(p.link!= None):
			prev = p
			p=p.link
		prev.link= None	
def del_at_middle(data):
	global start
	if(start == None):
		print('list is empty')
	else:
		p = start
		prev = None
		while(p.info != data):
			prev = p
			p = p.link
		store = p.link
		p.link = None
		prev.link = store
		
		
def del_at_position(pos):
	global start
	global count	
	if(start == None):
		print("list is empty to delete")
	else:
		p = start
		prev = None
		prev = p
		while(p.link!=None):
			if(pos == count):
				store = p.link
				p.link = None
				prev.link = store
				count = 0
				break
				
			else:
				prev = p
				p = p.link
				count = count+1
			
			

		       
def display():
	if(start == None):
		print("list is empty")
	else:
		p = start
		while(p!=None):
			print(p.info)
			p = p.link


def reverse_display():
	global start
	if(start == None):
		print("list is empty")
	else:
		prev = None
		current = start
		while(current!=None):
			next = current.link
			current.link = prev
			prev = current
			current = next
		start = prev
	display()
"""def reverse_display():
    global start
    prev = None
    current = start
    while current is not None:
        next_node = current.link
        current.link = prev
        prev = current
        current = next_node
    start = prev
    display()"""
			
     
     
while True:
    print("1. Enter the node at the beginning")
    print("2. Enter the node at the end")
    print("3. Enter the node in the middle")
    print("4. Delete the node at the beginning")
    print("5. Delete the node at the end")
    print("6. Delete the node in the middle")
    print("7. Display all the elements")
    print("8. Reverse display")
    print("9. Enter the position to add the node")
    print("10.Enter the position to del the node\n\n\n")
    choice = int(input("select the operation:"))
    if(choice == 1):
        data = int(input("Enter the node at beg: "))
        add_at_beg(data)
    elif(choice == 2):
        data = int(input("enter the node at last:"))
        add_at_end(data)
    elif(choice == 3):
    	data = int(input('enter the node in middle:'))
    	add_at_middle(data)
    elif(choice == 4):
    	del_at_beg()
    elif(choice == 5):
    	del_at_end()
    elif(choice == 6):
    	data = int(input("Enter the node to deleted: "))
    	del_at_middle(data)
    elif(choice == 7):
    	display()
    elif(choice == 8):
    	reverse_display()
    elif(choice == 9):
    	data = int(input("enter the node to add in position:"))
    	pos = int(input("enter the position:"))
    	add_at_position(data,pos)
    elif(choice == 10):
    	pos = int(input("Enter the position to delete the node:"))
    	del_at_position(pos)
    else:
        break
'''


#import pdb
#breakpoint()
class Node:
    def _init_(self,info):
        self.info = info
        self.prev_link = None
        self.next_link = None
    
start=None
count = 0

def add_at_beg(data):
    global start
    temp = Node(data)
    if(start == None):
        start = temp
    else:
        temp.next_link = start
        start.prev_link = temp
        start = temp

    
def add_at_end(data):
    global start
    temp = Node(data)
    if(start == None):
        start = temp
    else:
        p = start
        while(p.next_link!=None):
            back = p
            p=p.next_link
        p.next_link = temp
        temp.prev_link = back
    
def add_at_position(data,pos):
    global start
    global count
    temp = Node(data)
    if(start == None):
        start = temp
    else:
        p = start
        back = p.prev_link
        while(p.next_link!=None):
            if(pos == count):
                temp.prev_link = back
                back.next_link = temp
                temp.next_link = p
                p.prev_link = temp
                count = 0
                break
            else:
                back = p
                p = p.next_link
                count = count+1


def del_at_beg():
    global start
    if(start == None):
        print("List is empty to delete")
    else:
        p = start
        p.prev_link = None
        start = start.next_link
           
def del_at_end():
    global start
    if(start == None):
        print("List is empty to delete")
    else:
        p = start
        while(p.next_link!=None):
            back = p
            p = p.next_link
        back.next_link = None

def del_at_position(pos):
    global start
    global count
    if(start == None):
        print("list is empty to delete")
    else:
        p = start
        back = p.prev_link
        while(p.next_link!=None):
            if(pos == count):
                back.next_link = p.next_link
                p.prev_link = back
                count = 0
                break
            else:
                back = p
                p = p.next_link
                count = count+1



def display():
    global start
    if(start == None):
        print("list is empty to display")
    else:
        p = start
        while(p.next_link!=None):
            print(p.info)
            p=p.next_link
        print(p.info)

def reverse_display():
    global start
    if(start == None):
        print("list is empty")
    else:
        p = start
        current = start
        #back = current.prev_link
        while(current.next_link!=None):
            front = current.next_link
            back = current.prev_link
            current.prev_link = front
            current.next_link = back
            current = current.prev_link
        start = current.prev_link
        print("reversed linked list is:")
        print(current.info)
        display()


while(True):

    print("\n1.add node at beg")
    print("2.add node at end")
    print("3.add node in position")
    print("4.delete node at beg")
    print("5.delete node at end")
    print("6.del node in position")
    print("7.display list")
    print("8.Reverse the linked list")
    print("9.Exit\n\n")

    choice = int(input("select the operation: "))
    if(choice == 1):
        data = int(input("enter the node to add at beg: "))
        add_at_beg(data)
    elif(choice == 2):
        data = int(input("enter the node to add at end: "))
        add_at_end(data)
    elif(choice == 3):
        data = int(input("enter the node to add in pos: "))
        pos = int(input("enter the position to add: "))
        add_at_position(data,pos)
    elif(choice == 4):
        del_at_beg()
    elif(choice == 5):
        del_at_end()
    elif(choice == 6):
        pos = int(input("enter the position to del: "))
        del_at_position(pos)
    elif(choice == 7):
        display()
    elif(choice == 8):
        reverse_display()
    elif(choice == 9):
        break
    else:
        print("Enter the valid choice")

