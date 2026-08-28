
import pytest
from ansible.module_utils.common.network import to_netmask

def is_masklen(val):
    val = int(val)
    return 0 <= val <= 32 and val % 8 == 0

@pytest.mark.parametrize("setup, expected", [
    ("24", "255.255.255.0"),
    ("30", "255.255.255.252"),
])
def test_valid_case(setup, expected):
    assert to_netmask(setup) == expected

@pytest.mark.parametrize("invalid_val", ["33"])
def test_invalid_case(invalid_val):
    with pytest.raises(ValueError) as excinfo:
        to_netmask(invalid_val)
    assert str(excinfo.value) == 'invalid value for masklen'
