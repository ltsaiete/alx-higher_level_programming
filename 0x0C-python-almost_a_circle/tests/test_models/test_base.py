import unittest
from models import base
from models.base import Base
from models.rectangle import Rectangle


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

    def testJson(self):
        rect = Rectangle(2, 4, id=20)
        dictionary = rect.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(
            '[{"id": 20, "width": 2, "height": 4, "x": 0, "y": 0}]',
            json_dict
        )
        self.assertEqual('[]', Base.to_json_string(None))

    def testSave(self):
        r1 = Rectangle(10, 7, 2, 8, id=20)
        r2 = Rectangle(2, 4, id=21)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            r1_dict = '{"id": 20, "width": 10, "height": 7, "x": 2, "y": 8}'
            r2_dict = '{"id": 21, "width": 2, "height": 4, "x": 0, "y": 0}'
            self.assertEqual(
                f'[{r1_dict}, {r2_dict}]',
                file.read()
            )

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                '[]',
                file.read()
            )

    def testFromJson(self):
        self.assertEqual(

            [{"id": 20, "width": 2, "height": 4, "x": 0, "y": 0}],
            Rectangle.from_json_string(
                '[{"id": 20, "width": 2, "height": 4, "x": 0, "y": 0}]')
        )
        self.assertEqual(

            [],
            Rectangle.from_json_string(
                '')
        )
        self.assertEqual(

            [],
            Rectangle.from_json_string(None)
        )

    def testCreateRect(self):
        r1 = Rectangle(3, 5, 1, id=20)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual('[Rectangle] (20) 1/0 - 3/5', r1.__str__())
        self.assertEqual('[Rectangle] (20) 1/0 - 3/5', r2.__str__())
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def testLoadFile(self):
        rects_list = Rectangle.load_from_file()
        self.assertEqual([], rects_list)
        r1 = Rectangle(10, 7, 2, 8, id=20)
        r2 = Rectangle(2, 4, id=21)
        Rectangle.save_to_file([r1, r2])

        rects_list = Rectangle.load_from_file()
        self.assertEqual('[Rectangle] (20) 2/8 - 10/7',
                         rects_list[0].__str__())
        self.assertEqual('[Rectangle] (21) 0/0 - 2/4', rects_list[1].__str__())
