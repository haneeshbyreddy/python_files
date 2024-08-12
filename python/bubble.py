def bubble_sort(list2) :
	for i in range(0,len(list2)-1) :
		for j in range(i+1,len(list2)) :
			if list2[i]>list2[j]:
				temp=list2[i]
				list2[i]=list2[j]
				list2[j]=temp
	return list2

