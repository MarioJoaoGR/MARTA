
import pytest
from string_utils.validation import is_ip_v4

def test_out_of_range():
    assert not is_ip_v4('nope')  # returns False (not an IP)
    assert not is_ip_v4('255.200.100.999')  # returns False (number out of range)
    assert not is_ip_v4('256.200.100.75')  # returns False (first number out of range)
    assert not is_ip_v4('255.200.100')  # returns False (not enough numbers)
    assert is_ip_v4('255.200.100.75')  # returns True
