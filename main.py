def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    bot_token = "NDUzNjQyNDU0MDg0NjE2MTkz.GWnZjY.0fioW1AZBHJMGUq8bKGZ2D7rlwPE7zE2HiUD68"
    secret = "50219f7e69db39d1425ead93d550068632fefc77"
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    print("Result:", result)

if __name__ == "__main__":
    main()
