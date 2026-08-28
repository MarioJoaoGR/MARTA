
import pytest
from ansible.module_utils.common.network import to_masklen


def test_invalid_case():
    val = "255.255.255"
    with pytest.raises(ValueError):
        to_masklen(val)