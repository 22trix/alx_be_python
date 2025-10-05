# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Required: test_addition ---
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)

    # --- Required: test_subtraction ---
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(3, 7), -4)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # --- Required: test_multiplication ---
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    # --- Required: test_divide ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertIsNone(self.calc.divide(10, 0))   # divide by zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)

if __name__ == "__main__":
    unittest.main()
