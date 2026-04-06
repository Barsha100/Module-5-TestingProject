"""test_calculator.py - unit tests for calculator.py."""

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.add(7, 3.5), 10.5)

    def test_subtraction(self):
        self.assertEqual(calculator.subtract(7, 3.5), 3.5)

    def test_multiplication(self):
        self.assertEqual(calculator.multiply(7, 3.5), 24.5)

    def test_division(self):
        self.assertEqual(calculator.divide(7, 3.5), 2.0)

    def test_string_concat(self):
        self.assertEqual(calculator.concat_as_strings(7, 3.5), "73.5")

    def test_swap(self):
        self.assertEqual(calculator.swap_values(15, 4), (4, 15))


if __name__ == "__main__":
    unittest.main()
