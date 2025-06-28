def lin(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr=[5,6,7,4,3,2,1,9]
target=int(input("Enter a number: "))
m=lin(arr,target)
if m == -1:
    print("Target not found")
else:
    print("Target found",m)