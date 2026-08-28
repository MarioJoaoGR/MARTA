
import pytest

def shitcode(s):
    return ''.join(
        (c if (0 < ord(c) < 256) else '?') for c in s
    )

def test_ascii_string():
    result = shitcode("Hello, World!")
    assert result == "Hello, World!"



def test_empty_string():
    result = shitcode("")
    assert result == ""

def test_special_ascii_characters():
    result = shitcode("!@#$%^&*()")
    assert result == "!@#$%^&*()"
