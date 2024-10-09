"""
This module defines the `App` class which handles a command-line calculator.
The calculator supports basic operations like add, subtract, multiply, and divide.
"""

from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

# Disabling the warning for too few public methods as this class only needs one public method for now
# pylint: disable=R0903
class App:
    """
    A simple command-line calculator app that handles basic arithmetic operations:
    add, subtract, multiply, and divide.
    """

    def __init__(self):
        """Initialize the command handler."""
        self.command_handler = CommandHandler()

    def start(self):
        """
        Start the calculator app, accepting user input for two numbers
        and an operation, and performing the calculation.
        """
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

            operation = input(
                "Enter the operation (add, subtract, multiply, divide) or 'quit' to exit: "
            )
            if operation.lower() == 'quit':
                print("Exiting the app. Goodbye!")
                break

            try:
                a = int(a)
                b = int(b)

                # Register and execute commands based on the operation
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
