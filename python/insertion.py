def insertion_sort(list4):
    for i in range(1, len(list4)):
        key = list4[i]
        j = i - 1
        while j >= 0 and list4[j] > key:
            list4[j + 1] = list4[j]
            j -= 1
        list4[j + 1] = key
    return list4

