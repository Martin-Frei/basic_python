def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
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
        print("Result:", add(value1, value2))
    elif operator == 2:
        print("Result:", sub(value1, value2))
    elif operator == 3:
        print("Result:", mult(value1, value2))
    elif operator == 4:
        print("Result:", divi(value1, value2))
    else:
        print("Invalid selection!")

except ValueError:
    print("Error: Please enter valid integers.")








