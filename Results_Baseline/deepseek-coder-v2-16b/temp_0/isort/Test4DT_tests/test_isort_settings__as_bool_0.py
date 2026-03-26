# Module: isort.settings
import pytest

from isort.settings import _as_bool


# Test cases for _as_bool function
def test_true_values():
    assert _as_bool('true') == True
    assert _as_bool('True') == True
    assert _as_bool('TRUE') == True
    assert _as_bool('t') == True
    assert _as_bool('T') == True
    assert _as_bool('yes') == True
    assert _as_bool('Yes') == True
    assert _as_bool('YES') == True
    assert _as_bool('y') == True
    assert _as_bool('Y') == True
    assert _as_bool('on') == True
    assert _as_bool('On') == True
    assert _as_bool('ON') == True
    assert _as_bool('1') == True

def test_false_values():
    assert _as_bool('false') == False
    assert _as_bool('False') == False
    assert _as_bool('FALSE') == False
    assert _as_bool('f') == False
    assert _as_bool('F') == False
    assert _as_bool('no') == False
    assert _as_bool('No') == False
    assert _as_bool('NO') == False
    assert _as_bool('n') == False
    assert _as_bool('N') == False
    assert _as_bool('off') == False
    assert _as_bool('Off') == False
    assert _as_bool('OFF') == False
    assert _as_bool('0') == False

def test_invalid_value():
    with pytest.raises(ValueError) as e:
        _as_bool('maybe')
    assert str(e.value) == "invalid truth value maybe"
