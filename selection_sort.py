def selection_sort(arr):
    n = len(arr)
    for pos in range(n):
        min=pos
        for i in range(pos+1,n):
            if arr[i] < arr[min]:
                min=i
        arr[pos],arr[min]=arr[min],arr[pos]
    print(arr)

arr=[5,6,7,4,3,2,1,9]
selection_sort(arr)


