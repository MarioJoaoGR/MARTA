# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import is_ip_v4

def test_is_ip_v4_valid():
    assert is_ip_v4('255.200.100.75') == True

def test_is_ip_v4_invalid_not_ip():
    assert is_ip_v4('nope') == False

def test_is_ip_v4_invalid_out_of_range():
    assert is_ip_v4('255.200.100.999') == False
