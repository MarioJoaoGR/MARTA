
import pytest
from sanic.utils import str_to_bool

def test_valid_true_values():
    assert str_to_bool("Y") == True
    assert str_to_bool("Yes") == True
    assert str_to_bool("1") == True
    assert str_to_bool("True") == True
    assert str_to_bool("ON") == True
    assert str_to_bool("ENABLE") == True

def test_valid_false_values():
    assert str_to_bool("N") == False
    assert str_to_bool("No") == False
    assert str_to_bool("0") == False
    assert str_to_bool("False") == False
    assert str_to_bool("OFF") == False
    assert str_to_bool("DISABLE") == False

def test_invalid_value():
    with pytest.raises(ValueError):
        str_to_bool("maybe")
