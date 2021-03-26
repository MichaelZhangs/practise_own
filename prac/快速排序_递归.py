def quickSort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [j for j in arr[1:] if j > pivot]

    return quickSort(less) + [pivot] + quickSort(greater)

arr = [9,8,7,6,3,1]
a = quickSort(arr)
print(a)