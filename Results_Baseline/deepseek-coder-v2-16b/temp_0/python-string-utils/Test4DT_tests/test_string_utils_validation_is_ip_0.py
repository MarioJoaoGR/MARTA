
# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import is_ip
import pytest
from typing import Any

@pytest.mark.parametrize("test_input, expected", [
    ('255.200.100.75', True),
    ('2001:db8:85a3:0000:0000:8a2e:370:7334', True),
    ('1.2.3', False),
    (' ', False),
    ('invalid ip address', False),
    ('256.256.256.256', False),  # Invalid IPv4 address
])
def test_is_ip(test_input: Any, expected: bool):
    assert is_ip(test_input) == expected
