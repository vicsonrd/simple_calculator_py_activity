# calculator_logic.py

def perform_calculation(num1_str, num2_str, operation):
    
    try:
        # Step 7: Use appropriate Exceptions to capture errors
        val1 = float(num1_str)
        val2 = float(num2_str)

        if operation == "Addition":
            return val1 + val2
        elif operation == "Subtraction":
            return val1 - val2
        elif operation == "Multiplication":
            return val1 * val2
        elif operation == "Division":
            if val2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return val1 / val2
        
    except ValueError:
        raise ValueError("Invalid input! Please enter numeric values.")