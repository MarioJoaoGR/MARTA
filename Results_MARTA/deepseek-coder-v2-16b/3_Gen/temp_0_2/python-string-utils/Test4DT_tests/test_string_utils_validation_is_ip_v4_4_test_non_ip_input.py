
import pytest
from string_utils.validation import is_ip_v4

def test_non_ip_input():
    # Test with a non-IP input
    assert not is_ip_v4('nope')  # returns False as expected

    # Test with an out-of-range IP segment
    assert not is_ip_v4('255.200.100.999')  # returns False as expected
