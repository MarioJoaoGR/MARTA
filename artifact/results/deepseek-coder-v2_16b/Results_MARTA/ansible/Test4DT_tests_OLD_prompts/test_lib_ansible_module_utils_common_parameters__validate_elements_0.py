
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.parameters import _validate_elements, DEFAULT_TYPE_VALIDATORS

# Test case 1: Validating a list of integers
def test_validate_integers():
    values = [1, 2, 3]
    validated_values = _validate_elements('int', 'numbers', values)
    assert all(isinstance(v, int) for v in validated_values), "Not all elements are integers"

# Test case 2: Validating a list of strings
def test_validate_strings():
    values = ['a', 'b', 'c']
    validated_values = _validate_elements('str', 'letters', values)
    assert all(isinstance(v, str) for v in validated_values), "Not all elements are strings"

# Test case 3: Validating a list of floats using a custom callable

# Test case 4: Validating a list of booleans (should raise an error since booleans are not allowed by default)

# Test case 5: Validating a list of mixed types (should raise an error since only integers are allowed)

# Test case 6: Validating a list of dictionaries where each dictionary has an integer key