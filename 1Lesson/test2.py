import unittest
from main import check

class TestCheck(unittest.TestCase):

    def test_check(self):
        self.assertEqual(check(2), True)
        self.assertEqual(check(3), False)
        self.assertFalse(check(3))
        self.assertTrue(check(6))
        self.assertTrue(check(220))
        self.assertTrue(not check(1))
        self.assertTrue(not check(3))
        self.assertFalse(check(57))


if __name__ == '__main__':
    unittest.main()
