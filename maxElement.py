def getMax(arr):
    i=1
    n=len(arr)
    max=arr[0]
    while(i<n):
        if arr[i]>max:
            max=arr[i]
        i+=1
    return max

print(getMax([4,6,2,23,7,19,5]))
