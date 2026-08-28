
import pytest
from ansible.plugins.filter.core import to_bool

def test_valid_inputs():
    assert to_bool('Yes') is True
    assert to_bool('On') is True
    assert to_bool('1') is True
    assert to_bool('True') is True
    assert to_bool(True) is True

def test_non_string_truthy():
    assert to_bool(True) is True
    assert to_bool(1) is True
