# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Calculator operations
operations = {
    '1': 'Addition',
    '2': 'Subtraction',
    '3': 'Multiplication',
    '4': 'Division',
}

# Calculator menu
def display_menu():
    print("Choose an operation:")
    for key, value in operations.items():
        print(f"{key}: {value}")

# Recursive calculator
def calculator():
    display_menu()
    choice = input("Enter the operation number: ")

    if choice in operations:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        print(f"Result: {result}")

    else:
        print("Invalid choice. Please choose a valid operation.")
    
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() == 'yes':
        calculator()
    else:
        print("Calculator program terminated.")

calculator()