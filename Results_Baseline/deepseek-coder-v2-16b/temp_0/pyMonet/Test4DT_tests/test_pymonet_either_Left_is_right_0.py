
# Module: pymonet.either
# test_either.py
from pymonet.either import Right
import pytest

@pytest.fixture
def right_instance():
    return Right(42)

def test_is_right_returns_true(right_instance):
    assert right_instance.is_right()

def test_map_method(right_instance):
    mapped_value = right_instance.map(lambda x: x * 2)
    assert mapped_value.value == 84

def test_bind_method(right_instance):
    mapped_bind_value = right_instance.bind(lambda x: x * 2)
    assert mapped_bind_value == 84

def test_is_right_after_creation(right_instance):
    assert right_instance.is_right()

def test_to_maybe_method(right_instance):
    maybe = right_instance.to_maybe()
    assert not maybe.is_nothing

def test_to_validation_method(right_instance):
    validation = right_instance.to_validation()
    assert validation.value == 42
