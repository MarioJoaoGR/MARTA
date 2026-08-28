
import pytest
from string_utils.validation import is_ip_v4

def test_is_ip_v4_basic():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('1.2.3') == False
    assert is_ip_v4('256.256.256.256') == False
    assert is_ip_v4('') == False
    assert is_ip_v4('   ') == False
