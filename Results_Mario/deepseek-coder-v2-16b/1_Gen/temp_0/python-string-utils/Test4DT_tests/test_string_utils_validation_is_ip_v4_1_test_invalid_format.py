
import re
from string_utils.validation import is_ip_v4

def test_invalid_format():
    # Test cases for invalid formats
    assert not is_ip_v4('nope')  # Not an IP address
    assert not is_ip_v4('255.200.100.999')  # Number out of range
    assert not is_ip_v4('256.200.100.75')  # First number out of range
    assert not is_ip_v4('255.200.100')  # Not enough numbers
    assert not is_ip_v4('192.168.1.1.1')  # Too many numbers
    assert not is_ip_v4('192.168.1')  # Missing number
    assert not is_ip_v4('a.b.c.d')  # Non-numeric characters
    assert not is_ip_v4('192.168.1.1 ')  # Trailing space
    assert not is_ip_v4(' 192.168.1.1')  # Leading space
