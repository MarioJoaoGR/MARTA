
import pytest
from ansible.module_utils.common.text.converters import to_text

# Test cases for handling nonstring objects with different strategies
def test_to_text_nonstring_strategies():
    # Using 'simplerepr' strategy, which should convert the string representation of the object
    result = to_text(None, nonstring='simplerepr')
    assert isinstance(result, str)
    assert result == "None"

    # Using 'empty' strategy, which should return an empty text string
    result = to_text(None, nonstring='empty')
    assert isinstance(result, str)
    assert result == ""

    # Using 'passthru' strategy, which should return the object passed in as is
    result = to_text("Hello", nonstring='passthru')
    assert isinstance(result, str)
    assert result == "Hello"

    # Using 'strict' strategy, which should raise a TypeError if the object is not a string type
    with pytest.raises(TypeError):
        to_text(None, nonstring='strict')

# Test cases for handling byte strings with different error strategies
def test_to_text_byte_string_error_strategies():
    # Testing 'surrogate_or_strict' strategy, which should use 'strict' if 'surrogateescape' is not available
    result = to_text(b'\xe4\xf6\xfc', encoding='latin-1', errors='surrogate_or_strict')
    assert isinstance(result, str)
    assert result == "äöü"

    # Testing 'surrogate_then_replace' strategy, which should use 'replace' for unencodable characters
    result = to_text(b'\xff', encoding='utf-8', errors='surrogate_then_replace')
    assert isinstance(result, str)