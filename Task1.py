def add(a, b):
    return a + b
def sub(a, b):
    return(a - b)
def mul(a, b):
    return a * b
def div(a, b):
    if b != 0:
       return a / b
    else: 0
    
while True:
    print("--- Calculation tutorial ---")
    print("+. Addition")
    print("-. Subtraction")
    print("*. Multiplication")
    print("/. Division")
    print("Ac. Exit")

    choice = input("Enter an operator(+,-,*,/, Ac for Exit): ")
    if choice == 'Ac':
        print("Thank you! see you again...")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", sub(num1, num2))
    elif choice == '*':
        print("Result:", mul(num1, num2))
    elif choice == '/':
        print("Result:", div(num1, num2))
    else:
        print("Invalid operator please choose the right operator ")