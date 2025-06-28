def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
    return arr

arr=[5,6,7,4,3,2,1,9]
print(bubble_sort(arr))