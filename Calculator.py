def calculate():
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'Can\'t divide by zero'
    else:
        return "Invalid operation, try again"


print("This calculator supports the four basic operations.")
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
