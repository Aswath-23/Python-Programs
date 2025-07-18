def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot=arr[0]
        left=[x for x in arr[1:] if x < pivot]
        right=[x for x in arr[1:] if x>=pivot]
        return quickSort(left) + [pivot] + quickSort(right)

arr=[5,6,7,4,3,2,1,9]
print(quickSort(arr))
