import unittest
from circles import circle_area
from math import pi


class CircleAreaTest(unittest.TestCase):
    # Test areas when r >= 0
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0.0)
        self.assertAlmostEqual(circle_area(2.1), pi*(2.1**2))

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+3j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
