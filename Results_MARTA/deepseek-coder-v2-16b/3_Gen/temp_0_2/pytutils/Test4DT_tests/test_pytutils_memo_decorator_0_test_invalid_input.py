
import pytest
from unittest.mock import patch, MagicMock
from cachetools import cached

class MyClass:
    def expensive_calculation(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Inputs must be integers")
        return a + b

def decorator(method):
    # Implementation of the decorator as provided
    pass  # Continue with the rest of the implementation

@pytest.fixture
def my_class():
    return MyClass()

@pytest.mark.parametrize("a, b, expected_exception", [
    (3, "4", ValueError),
    ("3", 4, ValueError),
])
def test_invalid_input(my_class, a, b, expected_exception):
    with pytest.raises(expected_exception):
        my_class.expensive_calculation(a, b)
