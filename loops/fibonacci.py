def fibonacci(n):
    count = 3
    if n==1:
        return [1]
    elif n==2:
        return [1,1]
    i,j,k=1,1,2
    arr=[1,1,2]
    while count<n:
        i=j
        j=k
        k=i+j
        arr.append(k)
        count+=1
    return arr

print(fibonacci(9))
