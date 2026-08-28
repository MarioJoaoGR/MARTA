
import pytest
from keyword import iskeyword

def _validate_variable_keys(ds):
    for key in ds:
        if not iskeyword(key) and not key.isidentifier():
            raise TypeError("'%s' is not a valid variable name" % key)

# Test scenarios

def test_valid_keys():
    ds = {'valid_key': 'value'}
    _validate_variable_keys(ds)
    assert True  # If no error was raised, the test passes

def test_invalid_keys():
    with pytest.raises(TypeError):
        ds = {'1key': 'value'}
        _validate_variable_keys(ds)

def test_empty_dict():
    ds = {}
    _validate_variable_keys(ds)
    assert True  # If no error was raised, the test passes
