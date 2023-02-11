import unittest
from models import rectangle
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def testDocs(self):
        self.assertTrue(len(rectangle.__doc__) > 15)
        self.assertTrue(len(Rectangle.__doc__) > 15)

    def testAttributes(self):
        rect = Rectangle(2, 4, id=15)
        self.assertEqual(15, rect.id)

    def testGetters(self):
        rect = Rectangle(2, 4)
        self.assertEqual(2, rect.get_width())
        self.assertEqual(4, rect.get_height())
        self.assertEqual(0, rect.get_x())
        self.assertEqual(0, rect.get_y())

    def testSetters(self):
        rect = Rectangle(2, 4)
        rect.set_width(5)
        rect.set_height(10)
        rect.set_x(2)
        rect.set_y(2)

        self.assertEqual(5, rect.get_width())
        self.assertEqual(10, rect.get_height())
        self.assertEqual(2, rect.get_x())
        self.assertEqual(2, rect.get_y())

    def testTypes(self):
        with self.assertRaises(TypeError) as context:
            Rectangle('Hello', 4)
        self.assertEqual(str(context.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as context:
            Rectangle(4, 'Hello')
        self.assertEqual(str(context.exception), 'height must be an integer')

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 4, 'Hello', 0)
        self.assertEqual(str(context.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 4, 0, 'Hello')
        self.assertEqual(str(context.exception), 'y must be an integer')

    def testValues(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertEqual(str(context.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as context:
            Rectangle(2, 0)
        self.assertEqual(str(context.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as context:
            Rectangle(2, 4, -1, 0)
        self.assertEqual(str(context.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as context:
            Rectangle(2, 4, 0, -1)
        self.assertEqual(str(context.exception), 'y must be >= 0')

    def testSettersTypes(self):
        with self.assertRaises(TypeError) as context:
            rect = Rectangle(2, 4)
            rect.set_width('Hello')
        self.assertEqual(str(context.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as context:
            rect = Rectangle(2, 4)
            rect.set_height('Hello')
        self.assertEqual(str(context.exception), 'height must be an integer')

        with self.assertRaises(TypeError) as context:
            rect = Rectangle(2, 4)
            rect.set_x('Hello')
        self.assertEqual(str(context.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as context:
            rect = Rectangle(2, 4)
            rect.set_y('Hello')
        self.assertEqual(str(context.exception), 'y must be an integer')

    def testSettersValues(self):
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(2, 4)
            rect.set_width(0)
        self.assertEqual(str(context.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as context:
            rect = Rectangle(2, 4)
            rect.set_height(0)
        self.assertEqual(str(context.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as context:
            rect = Rectangle(2, 4)
            rect.set_x(-1)
        self.assertEqual(str(context.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as context:
            rect = Rectangle(2, 4)
            rect.set_y(-1)
        self.assertEqual(str(context.exception), 'y must be >= 0')

    def testArea(self):
        rect = Rectangle(2, 4)
        self.assertEqual(8, rect.area())

    def testStr(self):
        rect = Rectangle(2, 4, id=10)
        self.assertEqual('[Rectangle] (10) 0/0 - 2/4', rect.__str__())

    def testUpdate(self):
        rect = Rectangle(2, 4)
        rect.update(89)
        self.assertEqual('[Rectangle] (89) 0/0 - 2/4', rect.__str__())

        rect.update(89, 3)
        self.assertEqual('[Rectangle] (89) 0/0 - 3/4', rect.__str__())

        rect.update(89, 3, 5)
        self.assertEqual('[Rectangle] (89) 0/0 - 3/5', rect.__str__())

        rect.update(89, 3, 5, 2)
        self.assertEqual('[Rectangle] (89) 2/0 - 3/5', rect.__str__())

        rect.update(89, 3, 5, 2, 1)
        self.assertEqual('[Rectangle] (89) 2/1 - 3/5', rect.__str__())

        rect.update(width=2)
        self.assertEqual('[Rectangle] (89) 2/1 - 2/5', rect.__str__())

        rect.update(height=6)
        self.assertEqual('[Rectangle] (89) 2/1 - 2/6', rect.__str__())

        rect.update(x=4)
        self.assertEqual('[Rectangle] (89) 4/1 - 2/6', rect.__str__())

        rect.update(y=4)
        self.assertEqual('[Rectangle] (89) 4/4 - 2/6', rect.__str__())

        rect.update(id=3)
        self.assertEqual('[Rectangle] (3) 4/4 - 2/6', rect.__str__())

        rect.update(width=10, height=12, x=1, y=1, id=90)
        self.assertEqual('[Rectangle] (90) 1/1 - 10/12', rect.__str__())

    def testDictionary(self):
        rect = Rectangle(2, 4, id=19)
        self.assertEqual({
            'id': 19,
            'width': 2,
            'height': 4,
            'x': 0,
            'y': 0
        }, rect.to_dictionary())
