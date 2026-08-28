
import pytest
from ansible.module_utils.common.text.converters import to_text

# Test cases for handling non-string objects with different strategies
def test_to_text_nonstring_strategies():
    # Using 'simplerepr' strategy, which converts the object to its string representation and ensures it's a text string
    result = to_text(None, nonstring='simplerepr')
    assert isinstance(result, str)
    assert result == "None"

    # Using 'passthru' strategy, which returns the object passed in
    result = to_text("Hello", nonstring='passthru')
    assert isinstance(result, str)
    assert result == "Hello"

    # Using 'empty' strategy, which returns an empty text string
    result = to_text("", nonstring='empty')
    assert isinstance(result, str)
    assert result == ""

    # Using 'strict' strategy, which raises a TypeError if the object is not a string type
    with pytest.raises(TypeError):
        to_text(None, nonstring='strict')

# Test cases for handling byte strings with different encoding and error strategies
def test_to_text_byte_string_encoding_errors():
    # Testing with 'latin-1' encoding and 'surrogate_or_replace' error strategy
    result = to_text(b'\xe4\xf6\xfc', encoding='latin-1', errors='surrogate_or_replace')
    assert isinstance(result, str)
    assert result == "äöü"

    # Testing with 'utf-8' encoding and 'strict' error strategy (default for utf-8)
    with pytest.raises(UnicodeDecodeError):
        to_text(b'\xe4\xf6\xfc', encoding='utf-8', errors='strict')

# Test cases for handling byte strings with surrogate error handling
def test_to_text_byte_string_surrogate_error_handling():
    # Testing with 'utf-8' encoding and 'surrogate_or_strict' error strategy
    result = to_text(b'\xff', encoding='utf-8', errors='surrogate_or_strict')
    assert isinstance(result, str)