
import pytest
from unittest.mock import patch
from ansible.inventory.group import Group, to_safe_group_name


@patch('ansible.inventory.group.to_safe_group_name')
def test_sanitization_mocked(mock_to_safe_group_name):
    mock_to_safe_group_name.return_value = "valid_group_name"
    group = Group("invalid!group#name")
    assert group.name == "valid_group_name"

def test_serialize():
    group = Group("example_group")
    parent_group1 = Group("parent1")
    parent_group2 = Group("parent2")
    group.parent_groups.extend([parent_group1, parent_group2])
    
    expected_result = {
        "name": "example_group",
        "vars": {},
        "parent_groups": [
            {"name": "parent1", "vars": {}, "parent_groups": [], "depth": 0, "hosts": []},
            {"name": "parent2", "vars": {}, "parent_groups": [], "depth": 0, "hosts": []}
        ],
        "depth": 0,
        "hosts": []
    }
    
    assert group.serialize() == expected_result