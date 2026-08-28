
import pytest
from ansible.template.native_helpers import StrictUndefined
from collections.abc import Mapping, Sequence

# Define a custom exception for undefined values
class UndefinedError(Exception):
    pass

# Implement the _fail_on_undefined function
def _fail_on_undefined(data):
    if isinstance(data, Mapping):
        for value in data.values():
            _fail_on_undefined(value)
    elif isinstance(data, Sequence):
        for item in data:
            _fail_on_undefined(item)
    else:
        if isinstance(data, StrictUndefined):
            raise UndefinedError("The value is undefined.")
    return data

# Test function for valid input with a basic dictionary
def test_valid_input_basic_dictionary():
    data = {'a': 1, 'b': 2}
    assert _fail_on_undefined(data) == data

# Test function for error case when an undefined value is present
def test_error_case_with_undefined():
    data = {'a': 1, 'b': StrictUndefined()}
    with pytest.raises(UndefinedError):
        _fail_on_undefined(data)

# Test function for handling None input gracefully
def test_invalid_input_none():
    data = None
    assert _fail_on_undefined(data) is None
