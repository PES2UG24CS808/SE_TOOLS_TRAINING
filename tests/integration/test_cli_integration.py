"""
Integration Tests - CLI + Calculator Working Together
"""

from click.testing import CliRunner
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module (in-process)"""

    def run_cli(self, *args):
        """Invoke Click CLI in-process so coverage is measured."""
        from src.cli import calculate

        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    def test_cli_add_integration(self):
        res = self.run_cli("add", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "8"

    def test_cli_multiply_integration(self):
        res = self.run_cli("multiply", "4", "7")
        assert res.exit_code == 0
        assert res.output.strip() == "28"

    def test_cli_divide_integration(self):
        res = self.run_cli("divide", "15", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "5"

    def test_cli_sqrt_integration(self):
        res = self.run_cli("sqrt", "16")
        assert res.exit_code == 0
        assert res.output.strip() == "4"

    def test_cli_error_handling_integration(self):
        res = self.run_cli("divide", "10", "0")
        assert res.exit_code == 1
        assert "Division by zero is not allowed" in res.output

    def test_cli_invalid_operation_integration(self):
        res = self.run_cli("invalid", "1", "2")
        assert res.exit_code == 1
        assert "Unknown operation" in res.output


class TestCalculatorModuleIntegration:
    """Test calculator module functions work together"""

    def test_chained_operations(self):
        """Test using results from one operation in another"""
        from src.calculator import add, multiply, divide

        # Calculate (5 + 3) * 2 / 4
        step1 = add(5, 3)  # 8
        step2 = multiply(step1, 2)  # 16
        step3 = divide(step2, 4)  # 4

        assert step3 == 4.0

    def test_complex_calculation_integration(self):
        """Test complex calculation using multiple functions"""
        from src.calculator import power, square_root, add

        # Calculate sqrt(3^2 + 4^2) = 5 (Pythagorean theorem)
        a_squared = power(3, 2)  # 9
        b_squared = power(4, 2)  # 16
        sum_squares = add(a_squared, b_squared)  # 25
        hypotenuse = square_root(sum_squares)  # 5

        assert hypotenuse == 5.0
