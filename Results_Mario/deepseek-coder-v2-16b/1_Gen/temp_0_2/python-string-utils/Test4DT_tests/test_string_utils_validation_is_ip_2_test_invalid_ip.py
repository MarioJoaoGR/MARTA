
import pytest
from string_utils.validation import is_ip

@pytest.mark.parametrize("ip", [
    "1.2.3",  # Invalid IP address
])
def test_invalid_ip(ip):
    assert not is_ip(ip)
