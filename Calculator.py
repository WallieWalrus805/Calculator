def calculate():
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Invalid operation, try again"


print("This calculator supports the four basic operations and exponents.")
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print('ValueError: only numbers allowed')
    exit()
op = input("Enter operation: ")
try:
    num2 = float(input("Enter the first number: "))
except ValueError:
    print('ValueError: only numbers allowed')
    exit()
print(calculate())
