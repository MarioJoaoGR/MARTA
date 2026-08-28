# Module: pymonet.either
# test_right.py
from pymonet.either import Right
import pytest

@pytest.fixture
def right_instance():
    return Right(5)

def test_bind_with_valid_mapper(right_instance):
    def add_one(x):
        return x + 1
    result = right_instance.bind(add_one)
    assert result == 6

def test_bind_with_invalid_mapper(right_instance):
    def divide_by_zero(x):
        return x / 0
    with pytest.raises(ZeroDivisionError):
        right_instance.bind(divide_by_zero)

def test_bind_with_another_right_mapper(right_instance):
    def add_two(x):
        return Right(x + 2)
    result = right_instance.bind(add_two)
    assert isinstance(result, Right)
    assert result.value == 7

def test_bind_with_valid_mapper_returning_right(right_instance):
    def add_two(x):
        return Right(x + 2)
    result = right_instance.bind(add_two)
    assert isinstance(result, Right)
    assert result.value == 7
