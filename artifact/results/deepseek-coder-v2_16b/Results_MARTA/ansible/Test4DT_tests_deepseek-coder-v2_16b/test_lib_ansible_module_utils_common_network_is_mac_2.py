
import pytest
from ansible.module_utils.common.network import is_mac


def test_invalid_mac():
    invalid_macs = [
        "123456-789ABC",
        "1234.5678.9abc",
        "12:34:56:78:9A:BC:",
        "12:34:56:78:9A:BC:GH"
    ]
    for mac in invalid_macs:
        assert is_mac(mac) == False, f"Expected False for input '{mac}'"