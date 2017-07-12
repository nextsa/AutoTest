import unittest
class Point(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = string(y)
 
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
 
    def __eq__(self, other):
        return True if ((self.x == other.x) and (self.y == other.y)) else False
 
    def __ne__(self, other):
        return True if ((self.x != other.x) or (self.y != other.y)) else False
 
 
class TestPoint(unittest.TestCase):
    def setUp(self):
        self.A = Point(1, "one")
        self.B = Point(2, "two")
        self.C = Point(5, "undefined")
 
    def test_init(self):
        self.assertEqual((self.A.x, self.A.y), (int(1), str("one")), "Полученные значения не являются вещественными!!!")
        self.assertEqual((self.B.x, self.B.y), (int(2), str("two")),
                         "Полученные значения не являются вещественными!!!")
        self.assertEqual((self.C.x, self.C.y), (int(5), str("undefined")), "Полученные значения не являются вещественными!!!")
       
 
    def test_str(self):
        self.assertTrue(str(self.A) == "(1, one)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.B) == "(2, two)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.C) == "(3, undefined)", "Неправильный вывод на экран!!!")
 
 
if __name__ == '__main__':
    unittest.main()
