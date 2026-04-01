
from string_utils.validation import is_ip  # Assuming this import exists in the actual codebase
import pytest

@pytest.mark.parametrize("invalid_ip", [
    '1.2.3',          # Not enough octets for IPv4
    '256.256.256.256',# Invalid octet values for IPv4
    '2001:db8:85a3:0000:0000:8a2e:370:7334:', # Missing last hex part in IPv6
    '2001:db8:85a3:0000:0000:8a2e:370',      # Not enough parts for IPv6
    'not an ip address',                      # Clearly not an IP
    '',                                        # Empty string
    ' ',                                       # Whitespace-only string
])
def test_invalid_ip(invalid_ip):
    assert not is_ip(invalid_ip), f"Expected {invalid_ip} to be considered invalid, but it was identified as valid."
