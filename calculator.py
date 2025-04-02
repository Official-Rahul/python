def calculate(num1, num2, action):
    if action=="a":
        return num1 + num2
    elif action=="b":
        return num1 - num2
    elif action=="c":
        return num1 * num2
    else:
        return num1 / num2

def calculator():
    print("Simple Calculator")
    print("Enter a for Add")
    print("Enter b for Sub")
    print("Enter c for Mul")
    print("Enter d for Div")
    action=input("Type the option you want to perform? ")
    num1=int(input("Enter Num 1: "))
    num2=int(input("Enter Num 2: "))
    return calculate(num1, num2, action)

print(calculator())