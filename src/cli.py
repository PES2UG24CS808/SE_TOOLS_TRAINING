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
            result = add(num1, num2)

        elif operation == "subtract":
            result = subtract(num1, num2)

        elif operation == "multiply":
            result = multiply(num1, num2)

        elif operation == "divide":
            result = divide(num1, num2)

        elif operation == "power":
            result = power(num1, num2)

        elif operation == "square_root" or operation == "sqrt":
            result = square_root(num1)

        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # --- Output Formatting ---
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    # --- Exception Handling ---
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)

    except ZeroDivisionError:
        click.echo("Division by zero is not allowed")
        sys.exit(1)

    except Exception as e:  # pylint: disable=broad-exception-caught
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()  # pylint: disable=no-value-for-parameter
