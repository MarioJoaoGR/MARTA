
# Module: pymonet.either
# test_either.py
from pymonet.either import Right
import pytest

@pytest.fixture
def right_instance():
    return Right(42)

# Additional tests to cover uncovered line 125 and edge cases
def test_is_right_always_returns_true():
    # Test with a basic instance of Right
    right = Right(None)
    assert right.is_right()

    # Test with another type, ensuring it doesn't affect the method's behavior
    right = Right("string")
    assert right.is_right()

def test_is_right_method_documentation():
    # Ensure that the method documentation is correct and reflects its implementation
    right = Right(42)
    assert callable(right.is_right)
    assert isinstance(right.is_right(), bool)
    assert right.is_right() == True  # Simplified assertion based on method docstring

def test_map_method_with_lambda(right_instance):
    mapped_value = right_instance.map(lambda x: x * 2)
    assert mapped_value.value == 84

def test_bind_method_with_lambda(right_instance):
    mapped_bind_value = right_instance.bind(lambda x: x * 2)
    assert mapped_bind_value == 84

def test_to_maybe_method(right_instance):
    maybe = right_instance.to_maybe()
    assert not maybe.is_nothing

def test_to_validation_method(right_instance):
    validation = right_instance.to_validation()
    assert validation.value == 42
