import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    def testDocs(self):
        self.assertTrue(len(Base.__doc__) > 15)
        self.assertTrue(len(base.__doc__) > 15)

    def testId(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base()
        self.assertEqual(2, b2.id)
        b3 = Base()
        self.assertEqual(3, b3.id)
        b4 = Base(10)
        self.assertEqual(10, b4.id)
        b5 = Base()
        self.assertEqual(4, b5.id)
