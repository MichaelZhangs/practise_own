def shellSort(alist):
    #选择排序的分治实现
    n = len(alist)
    gap = n // 2

    while gap > 0:
        for j in range(gap,n):
            i = j
            while i > 0:
                if alist[i] < alist[ i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

lst = [ 64,12,9,46,37,21,8]
shellSort(lst)
print(lst)