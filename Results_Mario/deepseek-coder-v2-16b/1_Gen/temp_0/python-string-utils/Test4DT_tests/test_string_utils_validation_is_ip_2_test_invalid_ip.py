
import pytest
from unittest.mock import patch
from string_utils.validation import is_ip  # Assuming the module is named string_utils and contains validation functions

@pytest.mark.parametrize("invalid_ip", [
    '1.2.3',          # Not enough octets for IPv4
    '256.256.256.256',# Invalid octet values for IPv4
    '2001:db8:85a3:0000:0000:8a2e:370:7334:', # Missing last hex part in IPv6
    '2001:db8:85a3:0000:0000:8a2e:370',      # Not enough parts for IPv6
    ' ',            # Empty string, not a valid IP
    'not an ip'     # Clearly not an IP address
])
@patch('string_utils.validation.is_ip')  # Mocking the is_ip function to check its calls
def test_invalid_ip(mock_is_ip, invalid_ip):
    mock_is_ip.return_value = False  # Assuming is_ip returns False for invalid IPs
    assert not is_ip(invalid_ip)  # Assert that the function correctly identifies an invalid IP
