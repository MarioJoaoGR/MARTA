
import pytest
from pymonet.validation import Validation

# Scenario 1: Test standard input for Validation class with a valid value and no errors
def test_valid_input():
    val = Validation(value=10, errors=[])
    assert val.value == 10
    assert len(val.errors) == 0

# Scenario 2: Test edge case where the validation fails with an empty list of errors
def test_edge_case():
    val = Validation(None, [])
    assert val.value is None
    assert isinstance(val.errors, list) and not val.errors

# Scenario 3: Test invalid input handling for map method when mapper function raises an exception
def test_invalid_input():
    def failing_mapper(x):
        raise ValueError('Mapper failed')
    
    val = Validation(10, [])
    with pytest.raises(ValueError) as excinfo:
        mapped_val = val.map(failing_mapper)
    assert str(excinfo.value) == 'Mapper failed'
