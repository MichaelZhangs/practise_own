def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min = j
        for i in range(j + 1, n):
            if alist[min] > alist[i]:
                min = i
        alist[j], alist[min] = alist[min], alist[j]
        print(alist)
lst = [ 58,23,64,12,9,46,37,21,8]
select_sort(lst)
print(lst)