num = int(input("enter n: "))
for i in range(num,0,-1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()