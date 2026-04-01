
import re
from string_utils.validation import is_ip_v6
import pytest

def test_valid_ipv6():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?') == False
    assert is_ip_v6(' ') == False
