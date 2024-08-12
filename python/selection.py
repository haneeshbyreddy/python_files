def selection_sort(list3) :
	for j in range(0,len(list3)-1) :
		mini=j
		for i in range(j+1,len(list3)) :
			if list3[i] < list3[mini] :
				temp=list3[i]
				list3[i]=list3[mini]
				list3[mini]=temp
	return list3

