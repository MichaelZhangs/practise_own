def mergeSort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    #left归并排序后形成的有序的列表
    left = mergeSort(alist[:mid])
    right =  mergeSort(alist[mid:])
    # mergeSort(left,right)
    i, j = 0, 0
    res = [ ]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    print(res)
    return res


lst = [ 64,12,9,46,37,21,8]
ls =  mergeSort(lst)
print(ls)