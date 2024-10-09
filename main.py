from app import App

def perform_calculation(a, b, operation):
    try:
        a = int(a)
        b = int(b)
        if operation == 'add':
            return f"The result of {a} add {b} is equal to {a + b}"
        elif operation == 'subtract':
            return f"The result of {a} subtract {b} is equal to {a - b}"
        elif operation == 'multiply':
            return f"The result of {a} multiply {b} is equal to {a * b}"
        elif operation == 'divide':
            if b == 0:
                return "An error occurred: Cannot divide by zero"
            return f"The result of {a} divide {b} is equal to {a // b}"
        else:
            return f"Unknown operation: {operation}"
    except ValueError:
        return f"Invalid number input: {a} or {b} is not a valid number."



if __name__ == "__main__":
    app = App()  # Instantiate the App class
    app.start()  # Start the app (which will handle the calculations)
