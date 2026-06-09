
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

while(True):
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit" )
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result: ", add(a,b))
        case 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result: ", sub(a,b))
        case 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result: ", mul(a,b))
        case 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result: ", div(a,b))
        case 5:
            break
    
print("End")
