
import pytest
from string_utils.validation import is_ip_v4, SHALLOW_IP_V4_RE

def test_invalid_ipv4():
    # Test an invalid IP address due to out-of-range segment
    assert not is_ip_v4('255.200.100.999')  # returns False
    
    # Test a string that does not contain any dots, thus cannot be an IPv4 address
    assert not is_ip_v4('nope')  # returns False
    
    # Test an empty string, which should also return False as it's not considered a valid IP
    assert not is_ip_v4('')  # returns False
    
    # Test a string with only spaces, which should be invalid as well
    assert not is_ip_v4('   ')  # returns False
