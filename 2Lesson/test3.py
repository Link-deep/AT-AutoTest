# Проверяем на палиндром
import pytest
from main import isPalindrome

def test_isPalindrome_true():
    assert isPalindrome('madam') == True

def test_isPalindrome_false():
    assert isPalindrome('hello') == False

@pytest.mark.parametrize("test_input, expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True)
])
def test_isPalindrome(test_input, expected):
    assert isPalindrome(test_input) == expected

