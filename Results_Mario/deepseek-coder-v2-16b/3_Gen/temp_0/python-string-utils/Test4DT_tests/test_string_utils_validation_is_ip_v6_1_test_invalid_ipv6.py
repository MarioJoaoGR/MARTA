
import re
from string_utils.validation import is_ip_v6

def test_invalid_ipv6():
    # Test an invalid IPv6 address with an invalid character '?'
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?')
    
    # Test a string containing only whitespace characters
    assert not is_ip_v6(' ')
