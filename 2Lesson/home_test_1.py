import pytest
from home_main import count_vowels


def test_count_vowels():
    assert count_vowels("Hello, how are you?") == 8

def test_count_only_vowels():
    assert count_vowels("Eeo, ou ae you") == 10

def test_count_not_vowels():
    assert count_vowels("Hll, hw r ?") == 0

def test_count_vowels_lower():
    assert count_vowels("HEllO, how Are yoU?") == 8