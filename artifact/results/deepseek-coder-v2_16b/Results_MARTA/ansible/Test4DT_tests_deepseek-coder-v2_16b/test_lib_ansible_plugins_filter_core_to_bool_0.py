
import pytest
from ansible.plugins.filter.core import to_bool


def test_to_bool_boolean():
    assert to_bool(True) == True
    assert to_bool(False) == False

def test_to_bool_string_truthy():
    assert to_bool('Yes') == True
    assert to_bool('On') == True
    assert to_bool('1') == True
    assert to_bool('True') == True

def test_to_bool_string_falsy():
    assert to_bool('Off') == False
    assert to_bool('0') == False
    assert to_bool('False') == False


def test_to_bool_other_falsy():
    assert to_bool(0) == False
    assert to_bool(-0) == False  # Assuming -0 is falsy in this context