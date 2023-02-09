#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    def test_max(self):
        self.assertEqual(5, max_integer([1, 2, 3, 4, 5]))
        self.assertIsNone(max_integer())
        

    def test_type(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 'ALX'])
