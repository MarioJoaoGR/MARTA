
import pytest
from ansible.plugins.filter.urls import do_urlencode


def test_valid_dict_input():
    value = {"key": "value"}
    expected_output = 'key=value'
    result = do_urlencode(value)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"
