
import pytest
from ansible.inventory.group import to_safe_group_name


def test_edge_case_none():
    with pytest.raises(TypeError):
        to_safe_group_name()
