
import pytest
from ansible.modules.iptables import append_csv


def test_usage_with_non_string_values():
    mixed_list = [1, 2]
    with pytest.raises(TypeError):
        append_csv(mixed_list, [3, 4], 'numbers')