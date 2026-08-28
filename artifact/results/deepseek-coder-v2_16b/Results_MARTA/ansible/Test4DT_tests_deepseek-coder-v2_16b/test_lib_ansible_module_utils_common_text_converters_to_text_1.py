
import pytest
from ansible.module_utils.common.text.converters import to_text

def test_to_text_basic():
    # Test converting a byte string to a text string with UTF-8 encoding
    result = to_text(b'Hello, World!', 'utf-8')
    assert isinstance(result, str)
    assert result == 'Hello, World!'

    # Test handling errors by replacing invalid bytes
    result = to_text(b'\x80\x81', 'utf-8', errors='replace')
    assert isinstance(result, str)
    assert result == '\uFFFD'

    # Test converting a non-string object using the `simplerepr` strategy
    result = to_text({'key': 'value'})
    assert isinstance(result, str)
    assert result == "{'key': 'value'}"

    # Test converting a byte string with an unsupported encoding, handling errors by raising a TypeError
    with pytest.raises(TypeError):
        to_text(b'\x80\x81', 'ascii')

    # Test converting a text string without specifying encoding or errors, using the default values
    result = to_text('Hello, World!')
    assert isinstance(result, str)
    assert result == 'Hello, World!'

    # Test converting a byte string with surrogateescape error handling if supported, otherwise use strict
    result = to_text(b'\x80\x81', 'utf-8', errors='surrogate_or_strict')
    assert isinstance(result, str)
    assert result == '\uFFFD'  # Assuming surrogateescape is not supported and default error handling is used

    # Test converting a non-string object using the `empty` strategy
    result = to_text({'key': 'value'}, nonstring='empty')
    assert isinstance(result, str)
    assert result == ''

    # Test converting a byte string with surrogateescape error handling if supported, otherwise use replace
    result = to_text(b'\x80\x81', 'utf-8', errors='surrogate_or_replace')
    assert isinstance(result, str)
    assert result == '\uFFFD'  # Assuming surrogateescape is not supported and default error handling is used
