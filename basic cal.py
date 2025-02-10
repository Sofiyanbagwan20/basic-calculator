def basic_calculator():
    try:
        # Ask the user for two numbers
        num1 = eval((input("Enter the first number: ")))
        num2 = eval((input("Enter the second number: ")))

        # Ask the user for the operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the operation based on user input
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation. Please use one of +, -, *, /.")
            return

        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Run the calculator
basic_calculator()