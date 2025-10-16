import sys
import click

# Assuming src.calculator contains all these functions
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        # --- Operation Logic ---
        if operation == "add":
            if num2 is None:
                raise ValueError("Addition requires two operands")
            result = add(num1, num2)

        elif operation == "subtract":
            if num2 is None:
                raise ValueError("Subtraction requires two operands")
            result = subtract(num1, num2)

        elif operation == "multiply":
            if num2 is None:
                raise ValueError("Multiplication requires two operands")
            result = multiply(num1, num2)

        elif operation == "divide":
            if num2 is None:
                raise ValueError("Division requires two operands")
            # ZeroDivisionError is now correctly handled below
            result = divide(num1, num2)

        elif operation == "power":
            if num2 is None:
                raise ValueError("Power operation requires two operands")
            result = power(num1, num2)

        elif operation in ("square_root", "sqrt"):
            # square_root only needs one argument (num1)
            result = square_root(num1)

        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # --- Output Formatting ---
        # If the result is a whole number (e.g., 8.0), print as an integer (8)
        if result == int(result):
            click.echo(int(result))
        # Otherwise, format as a float with 2 decimal places
        else:
            click.echo(f"{result:.2f}")

    # --- Exception Handling ---
    except ValueError as e:
        # Handles errors like missing arguments
        click.echo(f"Error: {e}")
        sys.exit(1)

    except ZeroDivisionError:
        # Critical fix for integration test, handles division by zero
        click.echo("Division by zero is not allowed")
        sys.exit(1)

    except Exception as e:  # pylint: disable=broad-exception-caught
        # Catches all other unexpected runtime errors
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # The 'no-value-for-parameter' disable is necessary because click handles argument passing
    calculate()  # pylint: disable=no-value-for-parameter
