
import pytest
from ansible.utils.version import _Numeric

def test_valid_integer():
    num = _Numeric(10)
    assert repr(num) == '10'

def test_valid_string():
    num = _Numeric('20')
    assert repr(num) == '20'

def test_invalid_input():
    with pytest.raises(TypeError):
        num = _Numeric(None)
