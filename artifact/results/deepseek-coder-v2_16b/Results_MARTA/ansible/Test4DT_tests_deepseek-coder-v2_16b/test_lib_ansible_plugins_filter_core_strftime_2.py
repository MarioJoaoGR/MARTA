
import pytest
from ansible.plugins.filter.core import strftime
from ansible.errors import AnsibleFilterError
import time

def test_valid_strftime():
    # Test valid strftime call
    result = strftime('%Y-%m-%d %H:%M:%S', 1680579296.0)
    assert isinstance(result, str), "Expected a string result"
    assert len(result) > 0, "Expected non-empty string"

def test_invalid_epoch_value():
    # Test invalid epoch value raises AnsibleFilterError
    with pytest.raises(AnsibleFilterError):
        strftime('%Y-%m-%d %H:%M:%S', 'not_a_number')

def test_none_epoch_value():
    # Test None as epoch value should use current local time
    result = strftime('%Y-%m-%d %H:%M:%S')
    assert isinstance(result, str), "Expected a string result"
    assert len(result) > 0, "Expected non-empty string"
