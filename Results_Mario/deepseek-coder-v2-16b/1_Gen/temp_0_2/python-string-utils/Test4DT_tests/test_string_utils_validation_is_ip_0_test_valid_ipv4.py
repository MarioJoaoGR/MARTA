
import pytest
from string_utils.validation import is_ip

def test_valid_ipv4():
    assert is_ip('255.200.100.75') == True
    assert is_ip('192.168.1.1') == True
    assert is_ip('1.2.3') == False
