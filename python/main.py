from allmodules import *


class File1:
        with open("hemanth.txt", "r") as fopen:
            list1=[]
            lines = fopen.readline()
            list1.extend(map(int, lines.split()))
        fopen.close()



class Bubble_sort(File1) :
	def myfun(self) :
		print("Unsorted List : ",self.list1)
		bubble_sorted_list = self.list1.copy()
		y=bubble_sort(bubble_sorted_list)
		data="Sorted Bubble list is : ";
		write_file(data,y)
		


class Selection_sort(File1) :
	def myfun(self) :
		print("Unsorted List : ",self.list1)
		selection_sorted_list = self.list1.copy()
		y=selection_sort(selection_sorted_list)
		data="Sorted Selection list is : "
		#print("Sorted Selection sort : ",selection_sort(selection_sorted_list))
		write_file(data,y)
	


class Insertion_sort(File1) :
	def myfun(self) :
		print("Unsorted List : ",self.list1)
		insertion_sorted_list = self.list1.copy()
		y=insertion_sort(insertion_sorted_list)
		data="Sorted Insertion LIst is : "
		#print("Sorted Insertion sort : ",insertion_sort(insertion_sorted_list))
		write_file(data,y)
		
	
	

class Merge_sort(File1) :
	def myfun(self) :
		print("Unsorted List : ",self.list1)
		merge_sorted_list = self.list1.copy()
		y=merge_sort(merge_sorted_list)
		data="Sorted Merge List is : "
		#print("Sorted Merge sort : ",merge_sort(merge_sorted_list))
		write_file(data,y)
	
	
class Quick_sort(File1) :
	def myfun(self) :
		print("Unsorted List : ",self.list1)
		quick_sorted_list = self.list1.copy()
		y=merge_sort(quick_sorted_list)
		data="Sorted Quick List is : "
		#print("Sorted Quick sort : ",merge_sort(quick_sorted_list))
		write_file(data,y)
	
	
	
if __name__ == "__main__":
    num=1
    while num!=0 :
    	print("1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n4.Merge Sort\n5.Quick Sort\n0.Exit\n")

    	num=int(input("Enter the choice : "))
    	match (num):
    		case 1:
    			x=Bubble_sort()
    			x.myfun()
    		case 2:
    			x=Selection_sort()
    			x.myfun()
    		case 3:
    			x=Insertion_sort()
    			x.myfun()
    		case 4:
    			x=Merge_sort()
    			x.myfun()
    		case 5:
    			x=Quick_sort()
    			x.myfun()
    		case 0:
    			f=open("output.txt","w")
    			f.close()
    			print("Exiting The programm")
    		case _:
    			print("Invalid")
    
    	
