
import pytest
from sanic.utils import str_to_bool

def test_valid_true():
    assert str_to_bool("Y") == True
    assert str_to_bool("Yes") == True
    assert str_to_bool("1") == True

def test_valid_false():
    assert str_to_bool("N") == False
    assert str_to_bool("No") == False
    assert str_to_bool("0") == False
