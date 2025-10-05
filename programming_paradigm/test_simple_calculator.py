import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_add_floats(self):
        # use assertAlmostEqual for float results
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- Subtraction tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_to_negative(self):
        self.assertEqual(self.calc.subtract(3, 7), -4)

    def test_subtract_with_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    # --- Division tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_to_float(self):
        # dividing ints can return float
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)

if __name__ == "__main__":
    unittest.main()
