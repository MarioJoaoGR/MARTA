
import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.vars.host_group_vars import VarsModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group

def test_get_vars_default_cache():
    plugin = VarsModule()
    loader = MagicMock()
    path = "/path/to/inventory"
    entities = [Host('host1'), Group('group1')]

    with patch('os.path.exists', return_value=True):
        with patch('os.path.isdir', return_value=True):
            result = plugin.get_vars(loader, path, entities)
            assert isinstance(result, dict), "Expected a dictionary but got something else"

def test_get_vars_cache_disabled():
    plugin = VarsModule()
    loader = MagicMock()
    path = "/path/to/inventory"
    entities = [Host('host1'), Group('group1')]

    with patch('os.path.exists', return_value=True):
        with patch('os.path.isdir', return_value=True):
            result = plugin.get_vars(loader, path, entities, cache=False)
            assert isinstance(result, dict), "Expected a dictionary but got something else"

def test_get_vars_invalid_entity():
    plugin = VarsModule()
    loader = MagicMock()
    path = "/path/to/inventory"
    entities = [MagicMock()]

    with patch('os.path.exists', return_value=True):
        with patch('os.path.isdir', return_value=True):
            with pytest.raises(AnsibleParserError):
                plugin.get_vars(loader, path, entities)
