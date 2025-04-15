def nPowerX():
    x= int(input("Enter x: "))
    n = int(input("Enter n: "))

    result = 1
    if n==0:
        return result
    result = x
    for i in range(1, n):
        result = result * x
    return result

print(nPowerX())