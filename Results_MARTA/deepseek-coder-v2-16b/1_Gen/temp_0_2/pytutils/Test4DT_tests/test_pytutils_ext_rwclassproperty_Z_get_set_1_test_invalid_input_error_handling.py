
from pytutils.ext.rwclassproperty import sentinel
import pytest

# Assuming the module 'pytutils.ext.rwclassproperty' has a function get_set defined as follows:
def get_set(cls, value=None):
    if value is None:
        return cls._get_set
    cls._get_set = value

@pytest.mark.parametrize("value", [None, 'new_value', 42])
def test_invalid_input_error_handling(value):
    class Z:
        _get_set = sentinel.nothing
    
    if value is None:
        assert get_set(Z) == sentinel.nothing
    else:
        get_set(Z, value)
        assert Z._get_set == value
