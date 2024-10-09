# app/__init__.py

from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        while True:
            print("\n--- Calculator ---")
            a = input("Enter the first number (or 'quit' to exit): ")
            if a.lower() == 'quit':
                print("Exiting the app. Goodbye!")
                break

            b = input("Enter the second number: ")
            if b.lower() == 'quit':
                print("Exiting the app. Goodbye!")
                break

            operation = input("Enter the operation (add, subtract, multiply, divide) or 'quit' to exit: ")
            if operation.lower() == 'quit':
                print("Exiting the app. Goodbye!")
                break

            # Try to convert the input values to integers
            try:
                a = int(a)
                b = int(b)

                # Register commands based on the operation
                if operation == 'add':
                    self.command_handler.register_command("add", AddCommand(a, b))
                    result = self.command_handler.execute_command("add")
                elif operation == 'subtract':
                    self.command_handler.register_command("subtract", SubtractCommand(a, b))
                    result = self.command_handler.execute_command("subtract")
                elif operation == 'multiply':
                    self.command_handler.register_command("multiply", MultiplyCommand(a, b))
                    result = self.command_handler.execute_command("multiply")
                elif operation == 'divide':
                    if b == 0:
                        result = "Error: Cannot divide by zero."
                    else:
                        self.command_handler.register_command("divide", DivideCommand(a, b))
                        result = self.command_handler.execute_command("divide")
                else:
                    result = f"Unknown operation: {operation}"

                print(f"Result: {result}")

            except ValueError:
                print("Error: Invalid input. Please enter valid numbers.")
