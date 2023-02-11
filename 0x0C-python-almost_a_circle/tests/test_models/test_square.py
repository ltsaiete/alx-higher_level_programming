import unittest
from models import square
from models.square import Square


class TestSquare(unittest.TestCase):
    def testDocs(self):
        self.assertTrue(len(square.__doc__) > 15)
        self.assertTrue(len(Square.__doc__) > 15)

    def testInstance(self):
        sq = Square(4, id=16)
        self.assertEqual(16, sq.id)
        self.assertEqual(4, sq.get_width())
        self.assertEqual(4, sq.get_height())
        self.assertEqual(0, sq.get_x())
        self.assertEqual(0, sq.get_y())

        sq = Square(5, 2, 3, id=16)
        self.assertEqual(16, sq.id)
        self.assertEqual(5, sq.get_width())
        self.assertEqual(5, sq.get_height())
        self.assertEqual(2, sq.get_x())
        self.assertEqual(3, sq.get_y())

    def testStr(self):
        sq = Square(2, id=17)
        self.assertEqual('[Square] (17) 0/0 - 2', sq.__str__())

    def testSize(self):
        sq = Square(2)
        self.assertEqual(2, sq.get_size())
        self.assertEqual(2, sq.get_width())

        sq.set_size(4)
        self.assertEqual(4, sq.get_size())
        self.assertEqual(4, sq.get_width())

        with self.assertRaises(TypeError) as context:
            sq = Square(2)
            sq.set_size('Hello')
        self.assertEqual(str(context.exception), 'width must be an integer')

        with self.assertRaises(ValueError) as context:
            sq = Square(2)
            sq.set_size(0)
        self.assertEqual(str(context.exception), 'width must be > 0')

    def testUpdate(self):
        sq = Square(2)
        sq.update(89)
        self.assertEqual('[Square] (89) 0/0 - 2', sq.__str__())

        sq.update(89, 3)
        self.assertEqual('[Square] (89) 0/0 - 3', sq.__str__())

        sq.update(89, 3, 5)
        self.assertEqual('[Square] (89) 5/0 - 3', sq.__str__())

        sq.update(89, 3, 5, 2)
        self.assertEqual('[Square] (89) 5/2 - 3', sq.__str__())

        sq.update(size=2)
        self.assertEqual('[Square] (89) 5/2 - 2', sq.__str__())

        sq.update(x=4)
        self.assertEqual('[Square] (89) 4/2 - 2', sq.__str__())

        sq.update(y=4)
        self.assertEqual('[Square] (89) 4/4 - 2', sq.__str__())

        sq.update(id=3)
        self.assertEqual('[Square] (3) 4/4 - 2', sq.__str__())

        sq.update(size=10, x=1, y=1, id=90)
        self.assertEqual('[Square] (90) 1/1 - 10', sq.__str__())

    def testDictionary(self):
        sq = Square(4, id=19)
        self.assertEqual({
            'id': 19,
            'size': 4,
            'x': 0,
            'y': 0
        }, sq.to_dictionary())
