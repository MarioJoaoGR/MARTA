
import pytest
from ansible.module_utils.common.collections import text_type, binary_type
from unittest.mock import patch

def is_string(seq):
    """Identify whether the input has a string-like type (including bytes)."""
    return isinstance(seq, (text_type, binary_type)) or getattr(seq, '__ENCRYPTED__', False)

@pytest.mark.parametrize("input_data, expected", [
    ("Hello, World!", True),
    (b"Hello, World!", True),
    ([1, 2, 3], False),
   ({"key": "value"}, False)
])
def test_is_string(input_data, expected):
    assert is_string(input_data) == expected
