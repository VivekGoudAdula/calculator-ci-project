
# Unit Testing for Calculator Application

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(3, 2) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 2) == 8


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(5, 0) == "Error"
