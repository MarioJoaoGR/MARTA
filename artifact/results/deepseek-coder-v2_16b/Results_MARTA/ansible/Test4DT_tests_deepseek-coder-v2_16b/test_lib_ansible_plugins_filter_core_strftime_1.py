
import pytest
from ansible.plugins.filter import core
from ansible.errors import AnsibleFilterError
import time

def test_strftime_with_valid_format():
    # Test with a valid format string and optional epoch time
    result = core.strftime('%Y-%m-%d %H:%M:%S', 1680579296.0)
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 19, "Expected the length of the result to be 19 characters (YYYY-MM-DD HH:MM:SS)"

def test_strftime_without_epoch():
    # Test without providing an epoch time
    result = core.strftime('%Y-%m-%d %H:%M:%S')
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 19, "Expected the length of the result to be 19 characters (YYYY-MM-DD HH:MM:SS)"


def test_strftime_with_invalid_epoch_value():
    # Test with an invalid epoch value
    with pytest.raises(AnsibleFilterError):
        core.strftime('%Y-%m-%d %H:%M:%S', 'not_a_number')  # Invalid epoch value