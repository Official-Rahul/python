def factorial(n):
    i, result = 1, 1
    while(i<=n):
        result*=i
        i+=1
    return result

print(factorial(3))
print(factorial(5))