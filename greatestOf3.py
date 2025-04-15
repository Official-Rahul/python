def greatestOf3(num1, num2, num3):
    if num1>num2:
        if num3>num1:
            return num3
        else:
            return num1
    else:
        if num2>num3:
            return num2
        else:
            return num3

print(greatestOf3(6,2,4))