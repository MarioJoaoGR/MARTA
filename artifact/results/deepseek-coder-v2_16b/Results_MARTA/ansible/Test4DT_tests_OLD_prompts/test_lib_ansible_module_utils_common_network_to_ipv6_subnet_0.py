
import pytest
from ansible.module_utils.common.network import to_ipv6_subnet


def test_invalid_input():
    with pytest.raises(AttributeError):
        to_ipv6_subnet(None)