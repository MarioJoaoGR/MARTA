
import pytest
from sanic.utils import str_to_bool

def test_valid_true_values():
    assert str_to_bool("y") is True
    assert str_to_bool("yes") is True
    assert str_to_bool("YEP") is True
    assert str_to_bool("yup") is True
    assert str_to_bool("t") is True
    assert str_to_bool("true") is True
    assert str_to_bool("ON") is True
    assert str_to_bool("enable") is True
    assert str_to_bool("enabled") is True
    assert str_to_bool("1") is True

def test_valid_false_values():
    assert str_to_bool("n") is False
    assert str_to_bool("no") is False
    assert str_to_bool("f") is False
    assert str_to_bool("false") is False
    assert str_to_bool("OFF") is False
    assert str_to_bool("disable") is False
    assert str_to_bool("disabled") is False
    assert str_to_bool("0") is False

def test_invalid_value():
    with pytest.raises(ValueError):
        str_to_bool("maybe")
