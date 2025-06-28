arr=[1,2,3,4,5]
l=0
r=len(arr)-1
target=9
while l<r:
    res=arr[l]+arr[r]
    if (res==target):
        print(arr[l],arr[r])
        break
    elif (res<target):
        l=l+1
    elif (res>target):
        r=r-1

