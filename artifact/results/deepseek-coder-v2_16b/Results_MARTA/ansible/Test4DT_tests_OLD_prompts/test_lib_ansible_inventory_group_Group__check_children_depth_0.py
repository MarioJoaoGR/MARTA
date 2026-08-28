
import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.inventory.group import Group

def test_init_with_name():
    with patch('ansible.inventory.group.to_safe_group_name', return_value='sanitized_name'):
        g = Group("my-group_name")
        assert g.name == 'sanitized_name'

