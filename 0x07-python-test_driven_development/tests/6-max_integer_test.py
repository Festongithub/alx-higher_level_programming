#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([23, 45, 67, 89]), 89)

    def test_max_integer_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -3, -56, -890]), -1)

    def test_max_integer_duplicate_number(self):
        self.assertEqual(max_integer([333, 333, 333, 333]), 333)


if __name__ == "__main__":
    unittest.main()
