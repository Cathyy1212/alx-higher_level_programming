#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_numbers(self):
        """Test with floating-point numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

if __name__ == '__main__':
    unittest.main()
