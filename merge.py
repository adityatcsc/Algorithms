


def merge(l,r):
    result=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if ( l[i] < r[j] ):
            result.append( l[i] )
            i+=1
        else:
            result.append( r[j] )
            j+=1
    result +=l[i:]
    result +=r[j:]
    return result

def mergesort(lst):
    if (len(lst)<=1):
        return lst

    mid=int(len(lst)/2)
    left=mergesort(lst[:mid])
    right=mergesort(lst[mid:])
     
    return merge(left,right)

arr=[2,3,12,3,2,-1,0]

a=mergesort(arr)

print(arr)
print(a)