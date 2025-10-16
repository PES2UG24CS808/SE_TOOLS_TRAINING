"""
Integration Tests - CLI + Calculator Working Together
"""

import sys
import subprocess
from click.testing import CliRunner
import pytest


# -------------------------------------------------------------------------
# CLI Integration Tests (in-process & subprocess)
# -------------------------------------------------------------------------
class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Invoke Click CLI in-process so coverage is measured."""
        from src.cli import calculate
        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    def run_cli_subprocess(self, *args):
        """Run CLI as an external subprocess to simulate real execution."""
        cmd = [sys.executable, "-m", "src.cli"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        res = self.run_cli("add", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "8"

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        res = self.run_cli("multiply", "4", "7")
        assert res.exit_code == 0
        assert res.output.strip() == "28"

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        res = self.run_cli("divide", "15", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "5"

    def test_cli_sqrt_integration(self):
        """Test CLI can perform square root"""
        res = self.run_cli("sqrt", "16")
        assert res.exit_code == 0
        assert res.output.strip() == "4"

    def test_cli_error_handling_integration(self):
        """Test CLI properly handles calculator errors"""
        res = self.run_cli("divide", "10", "0")
        assert res.exit_code == 1
        assert "Division by zero is not allowed" in res.output

    def test_cli_invalid_operation_integration(self):
        """Test CLI handles invalid operations"""
        res = self.run_cli("invalid", "1", "2")
        assert res.exit_code == 1
        assert "Unknown operation" in res.output

    def test_cli_add_subprocess(self):
        """Verify CLI addition works via subprocess as well"""
        result = self.run_cli_subprocess("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_divide_by_zero_subprocess(self):
        """Ensure subprocess CLI handles division by zero"""
        result = self.run_cli_subprocess("divide", "10", "0")
        assert result.returncode == 1
        assert "Division by zero" in result.stdout


# -------------------------------------------------------------------------
# Calculator Module Integration Tests
# -------------------------------------------------------------------------
class TestCalculatorModuleIntegration:
    """Test calculator module functions work together"""

    def test_chained_operations(self):
        """Test using results from one operation in another"""
        from src.calculator import add, multiply, divide

        # Calculate (5 + 3) * 2 / 4
        step1 = add(5, 3)          # 8
        step2 = multiply(step1, 2)  # 16
        step3 = divide(step2, 4)    # 4

        assert step3 == 4.0

    def test_complex_calculation_integration(self):
        """Test complex calculation using multiple functions"""
        from src.calculator import power, square_root, add

        # Calculate sqrt(3^2 + 4^2) = 5 (Pythagorean theorem)
        a_squared = power(3, 2)       # 9
        b_squared = power(4, 2)       # 16
        sum_squares = add(a_squared, b_squared)  # 25
        hypotenuse = square_root(sum_squares)    # 5

        assert hypotenuse == 5.0
