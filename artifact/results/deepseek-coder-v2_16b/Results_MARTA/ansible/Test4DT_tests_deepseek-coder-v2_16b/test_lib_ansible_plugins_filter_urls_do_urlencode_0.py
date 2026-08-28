
import pytest
from ansible.plugins.filter.urls import do_urlencode


def test_empty_string():
    value = ""
    expected_output = ""
    result = do_urlencode(value)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_dictionary():
    value = {"key": "value"}
    expected_output = "key=value"
    result = do_urlencode(value)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
