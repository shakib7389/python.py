# Define the arithmetic functions
def add(a, b):
    print("addition")
    return a + b

def sub(a, b):
    print("subtraction")
    return a - b

def mul(a, b):
    print("multiplication")
    return a * b

def div(a, b):
    print("division")
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    while True:
        # Display the menu
        print("""
Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
""")
        # Get user choice
        choice = input("Enter the number of the operation: ").strip()
        if choice == '5':
            print("Exiting.")
            break
        if choice not in ('1','2','3','4'):
            print("Invalid choice. Please select 1–5.")
            continue

        # Get numbers, with validation
        try:
            a = float(input("Enter A: "))
            b = float(input("Enter B: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Perform the selected operation
        if choice == '1':
            result = add(a, b)
        elif choice == '2':
            result = sub(a, b)
        elif choice == '3':
            result = mul(a, b)
        else:  # choice == '4'
            result = div(a, b)

        print(f"Result: {result}")

# Start the calculator
if __name__ == "__main__":
    calculator()
