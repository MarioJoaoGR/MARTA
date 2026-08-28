
# Module: sanic.cookies
import pytest
from sanic.cookies import _quote

# Test cases for the _quote function

def test_normal_string():
    assert _quote("normal_string") == "normal_string"

def test_string_with_special_chars():
    assert _quote('special&char*') == '"special&char*"'

def test_none_input():
    assert _quote(None) is None

def test_string_with_double_quotes():
    assert _quote('quoted"string') == '"quoted\"string"'

# Additional test cases to cover edge cases and potential issues

def test_empty_string():
    assert _quote("") == '""'

def test_string_with_only_special_chars():
    assert _quote("!@#$%^&*()") == '"!@#$%^&*()"'

def test_already_quoted_string():
    assert _quote('"already"quoted') == '"\"already\"quoted"'

def test_string_with_backslashes():
    assert _quote("escaped\\test") == '"escaped\\\\test"'

# Negative tests to ensure the function handles incorrect inputs correctly

def test_non_string_input():
    with pytest.raises(TypeError):
        _quote(12345)  # Assuming non-string input should raise a TypeError
