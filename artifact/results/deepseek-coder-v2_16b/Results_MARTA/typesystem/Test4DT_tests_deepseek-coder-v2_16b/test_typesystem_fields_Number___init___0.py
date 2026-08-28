
import pytest
from typesystem.fields import Number

# Scenario 1: Test valid input with happy path parameters
def test_valid_input_happy_path():
    number = Number(minimum=0, maximum=10, exclusive_minimum=5, multiple_of=2)
    assert number.minimum == 0
    assert number.maximum == 10
    assert number.exclusive_minimum == 5
    assert number.multiple_of == 2

# Scenario 2: Test edge cases with no constraints
def test_edge_cases():
    number = Number(minimum=None, maximum=None, exclusive_minimum=10, exclusive_maximum=20)
    assert number.minimum is None
    assert number.maximum is None
    assert number.exclusive_minimum == 10
    assert number.exclusive_maximum == 20

# Scenario 3: Test invalid input with error handling
def test_invalid_input_error_handling():
    with pytest.raises(AssertionError):
        Number(minimum='a', maximum=[], exclusive_minimum={}, exclusive_maximum=True, multiple_of='b')
