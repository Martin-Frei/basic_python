def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

try:
    value1 = int(input('Your Number 1: '))
    value2 = int(input('Your Number 2: '))

    operator = int(input('''Please choose:
    1 = Addition
    2 = Subtraction
    3 = Multiplication
    4 = Division
    Your choice: '''))

    if operator == 1:
        print("Result:", addition(value1, value2))
    elif operator == 2:
        print("Result:", subtraction(value1, value2))
    elif operator == 3:
        print("Result:", multiplication(value1, value2))
    elif operator == 4:
        print("Result:", division(value1, value2))
    else:
        print("Invalid selection!")

except ValueError:
    print("Error: Please enter valid integers.")








