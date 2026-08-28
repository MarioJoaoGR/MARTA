
import pytest
from ansible.utils.version import _Numeric

def test_numeric_init_with_integer():
    num = _Numeric(10)
    assert num.specifier == 10

def test_numeric_init_with_string():
    num = _Numeric('10')
    assert num.specifier == 10

def test_numeric_init_with_none():
    with pytest.raises(TypeError):
        num_none = _Numeric(None)
