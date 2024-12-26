import pytest
from main import check


def test_check():
    assert check(6) == True

def test_check2():
   assert check(3) == False

# Поддержка параметризованных тестов. Это возможность запускать один и тот же тест
# с различными наборами данных с помощью специального декоратора.
@pytest.mark.parametrize("number, expected", [
   (2, True),
   (5, False),
   (0, True),
   (56, True),
   (-3, False)
])
def test_check3(number, expected):
   assert check(number) == expected