# Module: string_utils.validation
import re
import pytest
from string_utils.validation import is_ip_v6

# Define the regular expression for IPv6 address validation
IP_V6_RE = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

def is_full_string(input_string: str) -> bool:
    return bool(input_string and input_string.strip())

# Test cases for the `is_ip_v6` function
@pytest.mark.parametrize("test_input, expected", [
    ('2001:db8:85a3:0000:0000:8a2e:370:7334', True),  # Valid IPv6 address
    ('2001:db8:85a3:0000:0000:8a2e:370:?', False),   # Invalid character in the last position
    ('', False),                                      # Empty string
    (' ', False),                                     # String consisting only of whitespace characters
])
def test_is_ip_v6(test_input, expected):
    assert is_ip_v6(test_input) == expected
