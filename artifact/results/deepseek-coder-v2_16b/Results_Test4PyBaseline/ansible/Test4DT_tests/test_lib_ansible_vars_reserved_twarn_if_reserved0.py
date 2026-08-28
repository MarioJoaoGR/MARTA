
import pytest
from ansible.vars.reserved import warn_if_reserved

# Test cases for warn_if_reserved function

def test_warn_if_reserved_basic():
    with pytest.raises(Exception) as e_info:
        warn_if_reserved(['var1', 'var2', 'vars'])
    assert str(e_info.value) == "Found variable using reserved name: vars"

def test_warn_if_reserved_custom():
    custom_reserved = {'class', 'for'}
    with pytest.raises(Exception) as e_info:
        warn_if_reserved(['var1', 'var2', 'class'], additional=custom_reserved)
    assert str(e_info.value) == "Found variable using reserved name: class"

def test_warn_if_reserved_set():
    with pytest.raises(Exception) as e_info:
        warn_if_reserved(set(['var1', 'var2', 'vars']))
    assert str(e_info.value) == "Found variable using reserved name: vars"

def test_warn_if_reserved_no_warnings():
    with pytest.raises(Exception) as e_info:
        warn_if_reserved(['var1', 'var2'])
    assert str(e_info.value) == "Found variable using reserved name: vars"
