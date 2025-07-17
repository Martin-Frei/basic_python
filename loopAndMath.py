def askNumber():
    try:
        a = float(input("Your number: "))
        return a
    except ValueError:
        print("Input is not a number. Try again.")
        return askNumber()

def askOperator():
    operator = input("What operator? (+ - * / or q to quit): ")
    if operator.lower() == "q":
        print("👋 Bye bye!")
        exit()
    if operator not in ("+", "-", "*", "/"):
        print("Invalid operator. Try again.")
        return askOperator()
    return operator

def calculate(a, operator, b):
    if operator == "/" and b == 0:
        print("Division by zero not allowed.")
        return None
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/": return a / b

def mainCalculator():
    a = askNumber()
    operator = askOperator()
    b = askNumber()
    
    result = calculate(a, operator, b)
    if result is None:
        return

    print(f"Result: {result}")

    while True:
        askAhead = input("Another operation on result? (y/n): ").lower()
        if askAhead != "y":
            break

        operator = askOperator()
        b = askNumber()
        new_result = calculate(result, operator, b)
        if new_result is None:
            continue

        result = new_result
        print(f"New result: {result}")
        print("------")

if __name__ == "__main__":
    mainCalculator()
