def bin(arr,low,high,x):

    while high >= low:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            return bin(arr,mid+1,high,x)
        if arr[mid] > x:
            return bin(arr,low,mid-1,x)


arr=[1,2,3,4,5,6,7,8]
x=int(input('enter search element :'))
print(bin(arr,0,len(arr)-1,x))