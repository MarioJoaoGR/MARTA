
import re
import pytest
from string_utils.validation import is_ip_v4

def test_valid_ipv4():
    input_string = '255.200.100.75'
    assert is_ip_v4(input_string) == True, f"Expected {input_string} to be a valid IPv4 address"
