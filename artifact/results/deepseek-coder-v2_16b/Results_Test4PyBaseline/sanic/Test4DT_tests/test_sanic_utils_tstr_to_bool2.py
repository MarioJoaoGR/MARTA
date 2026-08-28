# Module: sanic.utils
import pytest
from sanic.utils import str_to_bool

def test_str_to_bool_true():
    assert str_to_bool("True") == True
    assert str_to_bool("yes") == True
    assert str_to_bool("yep") == True
    assert str_to_bool("yup") == True
    assert str_to_bool("t") == True
    assert str_to_bool("true") == True
    assert str_to_bool("on") == True
    assert str_to_bool("enable") == True
    assert str_to_bool("enabled") == True
    assert str_to_bool("1") == True

def test_str_to_bool_false():
    assert str_to_bool("False") == False
    assert str_to_bool("no") == False
    assert str_to_bool("f") == False
    assert str_to_bool("false") == False
    assert str_to_bool("off") == False
    assert str_to_bool("disable") == False
    assert str_to_bool("disabled") == False
    assert str_to_bool("0") == False

def test_str_to_bool_invalid():
    with pytest.raises(ValueError):
        str_to_bool("maybe")
