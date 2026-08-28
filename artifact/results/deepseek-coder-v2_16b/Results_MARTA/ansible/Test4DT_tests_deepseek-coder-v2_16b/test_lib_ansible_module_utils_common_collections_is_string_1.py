
import pytest
from ansible.module_utils.common.collections import text_type, binary_type

def is_string(seq):
    """Identify whether the input has a string-like type (including bytes)."""
    return isinstance(seq, (text_type, binary_type)) or getattr(seq, '__ENCRYPTED__', False)

# Test cases for different scenarios

@pytest.mark.parametrize("input_data", ["Hello, World!"])
def test_valid_string(input_data):
    assert is_string(input_data), f"Expected {input_data} to be recognized as string-like."

@pytest.mark.parametrize("input_data", [b"Hello, World!"])
def test_valid_bytes(input_data):
    assert is_string(input_data), f"Expected {input_data} to be recognized as string-like."

@pytest.mark.parametrize("input_data", [[1, 2, 3], {"key": "value"}])
def test_invalid_types(input_data):
    assert not is_string(input_data), f"Expected {input_data} to be recognized as not string-like."
