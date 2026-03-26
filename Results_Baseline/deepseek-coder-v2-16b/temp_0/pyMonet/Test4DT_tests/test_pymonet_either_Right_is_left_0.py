# Module: pymonet.either
# test_either.py
from pymonet.either import Right
import pytest

@pytest.fixture
def right_value():
    return Right(42)

def test_is_left_returns_false(right_value):
    assert not right_value.is_left()

def test_map_method(right_value):
    mapped_value = right_value.map(lambda x: x * 2)
    assert mapped_value.value == 84

def test_bind_method(right_value):
    mapped_bind_value = right_value.bind(lambda x: x * 2)
    assert mapped_bind_value == 84

def test_is_right(right_value):
    assert right_value.is_right()

def test_to_maybe(right_value):
    maybe = right_value.to_maybe()
    assert not maybe.is_nothing

def test_to_validation(right_value):
    validation = right_value.to_validation()
    assert validation.value == 42
