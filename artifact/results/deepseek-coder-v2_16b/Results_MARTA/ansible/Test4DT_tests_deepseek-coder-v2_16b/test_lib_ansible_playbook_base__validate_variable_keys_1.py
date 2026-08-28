
import pytest
from keyword import isidentifier

def _validate_variable_keys(ds):
    for key in ds:
        if not isidentifier(key):
            raise TypeError("'%s' is not a valid variable name" % key)

# Test scenarios

def test_valid_keys():
    ds = {'valid_key': 'value'}
    try:
        _validate_variable_keys(ds)
    except TypeError as e:
        pytest.fail("Test failed with unexpected error: {}".format(e))

def test_invalid_keys():
    ds = {'1key': 'value'}
    with pytest.raises(TypeError):
        _validate_variable_keys(ds)

def test_none_input():
    ds = None
    with pytest.raises(TypeError):
        _validate_variable_keys(ds)
