
import pytest
from pytutils.ext.rwclassproperty import sentinel

# Assuming the module 'pytutils.ext.rwclassproperty' has a function get_set defined as follows:
def get_set(cls, value=None):
    if value is None:
        return cls._get_set
    cls._get_set = value

@pytest.mark.parametrize("value, expected", [
    (None, sentinel.nothing),  # Test retrieval of the default value
    ('new_value', 'new_value'),  # Test setting and retrieving a new value
])
def test_valid_input_get(value, expected):
    class Z:
        _get_set = sentinel.nothing
    
    if value is None:
        assert get_set(Z) == expected
    else:
        get_set(Z, value)
        assert get_set(Z) == expected
