##calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("===== Simple Calculator =====")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'
    else:
        print("Invalid choice!")
        return

    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()