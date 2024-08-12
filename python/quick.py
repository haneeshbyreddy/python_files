def quick_sort(list6):
    lb = 0
    ub = len(list6) - 1
    quick(list6, lb, ub)
    
    return list6

def quick(list6, lb, ub):
    if lb < ub:
        loc = partition(list6, lb, ub)
        quick(list6, lb, loc - 1)
        quick(list6, loc + 1, ub)

def partition(list6, lb, ub):
    pivot = list6[ub]
    i = lb - 1

    for j in range(lb, ub):
        if list6[j] <= pivot:
            i += 1
            list6[i], list6[j] = list6[j], list6[i]

    list6[i + 1], list6[ub] = list6[ub], list6[i + 1]
    return i + 1
list6=[4111,22,4,2,11]
quick(list6,0,len(list6)-1)
print(list6)




