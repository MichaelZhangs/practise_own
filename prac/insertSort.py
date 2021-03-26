def insertSort(alist):
    #默认第一个有序，从后面无序的元素中依次与前面有序序列从后向前比较
    for i in range(1, len(alist)):
        j = i
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j -= 1
            else:
                break

lst = [ 64,12,9,46,37,21,8]
insertSort(lst)
print(lst)