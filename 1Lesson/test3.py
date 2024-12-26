import unittest
from main import divide3


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide3(4, 2), 2)
        self.assertEqual(divide3(20, 5), 4)
        self.assertNotEqual(divide3(4, 2), 3)

    def test_divide_by_zero(self):  #Проверка на ошибку ValueError, TypeError
        self.assertRaises(ValueError, divide3, 6, 0)

if __name__ == '__main__':
    unittest.main()
