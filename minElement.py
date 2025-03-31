def getMin(arr):
    i=1
    n=len(arr)
    min=arr[0]
    while(i<n):
        if(arr[i]<min):
            min=arr[i]
        i+=1
    return min

print(getMin([4,6,2,23,7,19,5]))
