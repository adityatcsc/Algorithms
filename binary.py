
def binary(arr,tar):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            l=mid+1
        else:
            r=mid-1
    return -1

arr=[2,4,7,8,9]

found=binary(arr,9)

print(found)