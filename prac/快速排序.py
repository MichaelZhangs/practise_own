def quickSort(arr,low, high):
    if low >= high:
        return
    i = low
    j = high
    p = arr[low]
    while i < j:
        if arr[j] >= p:
            j -= 1
        arr[i] = arr[j]
        if arr[i] < p:
            i += 1
        arr[j] = arr[i]
    arr[i] = p
    quickSort(arr, low, i - 1 )
    quickSort(arr, i+1, high)
    print(arr)
    print(id(arr))
a = [ 5,2,8,7,4,4]
quickSort(a, 0, len(a) -1 )
print("================")
print(a)
print(id(a))