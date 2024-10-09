# app/__init__.py
from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):
        # Initialize CommandHandler
        self.handler = CommandHandler()

    def start(self):
        # Main loop for user interaction
        while True:
            print("\n--- Calculator ---")
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            operation = input("Enter the operation (add, subtract, multiply, divide) or 'quit' to exit: ")

            if operation == 'quit':
                print("Exiting the app. Goodbye!")
                break

            result = self.perform_calculation(a, b, operation)
            print(f"Result: {result}")

    def perform_calculation(self, a, b, operation):
        try:
            a = int(a)  # Ensure 'a' is an integer
            b = int(b)  # Ensure 'b' is an integer

            # Register and execute commands based on user input
            if operation == 'add':
                self.handler.register_command('add', AddCommand(a, b))
                return self.handler.execute_command('add')
            elif operation == 'subtract':
                self.handler.register_command('subtract', SubtractCommand(a, b))
                return self.handler.execute_command('subtract')
            elif operation == 'multiply':
                self.handler.register_command('multiply', MultiplyCommand(a, b))
                return self.handler.execute_command('multiply')
            elif operation == 'divide':
                if b == 0:
                    return "Error: Cannot divide by zero."
                self.handler.register_command('divide', DivideCommand(a, b))
                return self.handler.execute_command('divide')
            else:
                return f"Unknown operation: {operation}"

        except ValueError:
            return "Error: Invalid input. Please enter valid numbers."
