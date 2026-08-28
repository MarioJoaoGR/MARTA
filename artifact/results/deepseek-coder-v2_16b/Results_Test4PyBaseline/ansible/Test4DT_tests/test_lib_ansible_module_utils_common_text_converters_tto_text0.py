
import pytest
from ansible.module_utils.common.text.converters import to_text

# Test cases for basic usage of the to_text function
def test_to_text_basic():
    result = to_text("Hello, World!")
    assert isinstance(result, str)
    assert result == "Hello, World!"

# Test cases for handling byte strings with different encoding and error strategies
def test_to_text_byte_string_encoding_errors():
    result = to_text(b'\xe4\xf6\xfc', encoding='latin-1', errors='surrogate_or_replace')
    assert isinstance(result, str)
    assert result == "äöü"

# Test cases for using nonstring strategy
def test_to_text_nonstring_strategy():
    result = to_text(None, nonstring='empty')
    assert isinstance(result, str)
    assert result == ""

# Test cases for handling byte strings with surrogate error handling
def test_to_text_byte_string_surrogate_error_handling():
    result = to_text(b'\xff', encoding='utf-8', errors='surrogate_or_strict')
    assert isinstance(result, str)