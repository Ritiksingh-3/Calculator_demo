def calculator():
    print("=== Simple Calculator ===")
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")

    try:
        choice = int(input("Enter your choice (1-7): "))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        operations = {
            1: a + b,
            2: a - b,
            3: a * b,
            4: a / b if b != 0 else "Error: Division by zero",
            5: a % b if b != 0 else "Error: Division by zero",
            6: a ** b,
            7: a // b if b != 0 else "Error: Division by zero"
        }

        result = operations.get(choice, "Invalid choice")
        print("Result =", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()