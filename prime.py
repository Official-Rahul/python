def isPrime(n):
    div = int(n/2)
    i=2
    while i<=div:
        if n%i==0:
            return False
        i+=1
    return True

if isPrime(9):
    print("prime!")
else:
    print("nope")