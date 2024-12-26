# Пример работы с unittest
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
    def test_subtract(self):
        self.assertEqual(3 - 2, 1)

# Пример работы с pytest:

import pytest

def test_add2():
    assert 1 + 1 == 2

def test_subtract():
    assert 3 - 2 == 1



