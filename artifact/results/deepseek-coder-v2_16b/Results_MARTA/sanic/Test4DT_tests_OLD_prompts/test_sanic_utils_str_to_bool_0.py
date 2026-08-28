
import pytest
from sanic.utils import str_to_bool

def test_valid_true_values():
    assert str_to_bool("Y") == True
    assert str_to_bool("Yes") == True
    assert str_to_bool("yep") == True
    assert str_to_bool("yup") == True
    assert str_to_bool("t") == True
    assert str_to_bool("true") == True
    assert str_to_bool("on") == True
    assert str_to_bool("enable") == True
    assert str_to_bool("enabled") == True
    assert str_to_bool("1") == True

def test_valid_false_values():
    assert str_to_bool("N") == False
    assert str_to_bool("No") == False
    assert str_to_bool("no") == False
    assert str_to_bool("f") == False
    assert str_to_bool("false") == False
    assert str_to_bool("off") == False
    assert str_to_bool("disable") == False
    assert str_to_bool("disabled") == False
    assert str_to_bool("0") == False
