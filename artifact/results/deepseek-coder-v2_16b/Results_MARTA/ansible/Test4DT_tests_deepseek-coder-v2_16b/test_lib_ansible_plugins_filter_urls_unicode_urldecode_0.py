
import pytest
from ansible.plugins.filter.urls import unicode_urldecode


def test_valid_input():
    string = "Hello%20World"
    expected_output = "Hello World"
    assert unicode_urldecode(string) == expected_output
