
import pytest
from flutils.codecs.raw_utf8_escape import _each_utf8_hex


def test_valid_ascii_input():
    text = "Hello, World!"
    expected_output = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
    result = list(_each_utf8_hex(text))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_empty_input():
    text = ""
    expected_output = []
    result = list(_each_utf8_hex(text))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"