
from string_utils.validation import is_ip  # Assuming this module contains the is_ip function
import pytest

def test_invalid_ip():
    assert not is_ip('1.2.3')  # This should return False as it's an invalid IP address
    assert not is_ip('notanipaddress')  # This should also return False as it's clearly not an IP address
