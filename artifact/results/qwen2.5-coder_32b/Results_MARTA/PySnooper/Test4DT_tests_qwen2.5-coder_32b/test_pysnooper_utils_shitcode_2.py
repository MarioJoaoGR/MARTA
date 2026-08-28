
import pytest

def shitcode(s):
    return ''.join(
        (c if (0 < ord(c) < 256) else '?') for c in s
    )




def test_ascii_only():
    input_string = "Hello, World!"
    expected_output = "Hello, World!"
    assert shitcode(input_string) == expected_output

def test_empty_string():
    input_string = ""
    expected_output = ""
    assert shitcode(input_string) == expected_output

def test_special_ascii_characters():
    input_string = "!@#$%^&*()"
    expected_output = "!@#$%^&*()"
    assert shitcode(input_string) == expected_output