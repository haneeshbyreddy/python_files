def merge(left, right, list5, mid, sec):
    i = j = k = 0

    while i < mid and j < sec:
        if left[i] <= right[j]:
            list5[k] = left[i]
            i += 1
        else:
            list5[k] = right[j]
            j += 1
        k += 1

    while i < mid:
        list5[k] = left[i]
        i += 1
        k += 1

    while j < sec:
        list5[k] = right[j]
        j += 1
        k += 1


def merge_sort(list5):
    if len(list5) < 2:
        return

    mid = len(list5) // 2

    left = list5[:mid]
    right = list5[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, list5, len(left), len(right))
    
    return list5
    
