# Module: ansible.vars.manager
import pytest
from ansible.inventory.host_list import Host, Group
from your_module import _get_plugin_vars  # Replace 'your_module' with the actual module name where _get_plugin_vars is defined
from ansible.errors import AnsibleError

# Mock plugin and entities for testing
class MockPlugin:
    def __init__(self, vars_data):
        self.vars_data = vars_data
    
    def get_vars(self, loader, path, entities):
        return self.vars_data
    
    def get_host_vars(self, host_name):
        return {'host_var': f'value_{host_name}'}
    
    def get_group_vars(self, group_name):
        return {'group_var': f'value_{group_name}'}

# Define test cases
@pytest.fixture
def mock_plugin():
    vars_data = {'common_var': 'common_value'}
    return MockPlugin(vars_data)

@pytest.mark.parametrize("path, entities, expected", [
    ('path/to/plugin', [Host('host1'), Group('group1')], {'common_var': 'common_value', 'host_var': 'value_host1', 'group_var': 'value_group1'}),
    (None, [Host('host1'), Group('group1')], {'common_var': 'common_value', 'host_var': 'value_host1', 'group_var': 'value_group1'}),
    ('path/to/plugin', [], {'common_var': 'common_value'}),
    (None, [], {'common_var': 'common_value'})
])
def test__get_plugin_vars(mock_plugin, path, entities, expected):
    plugin = mock_plugin
    result = _get_plugin_vars(plugin, path, entities)
    assert result == expected

# Test case for invalid plugin
def test__get_plugin_vars_invalid_plugin():
    class InvalidMockPlugin:
        pass
    
    plugin = InvalidMockPlugin()
    with pytest.raises(AnsibleError):
        _get_plugin_vars(plugin, 'path/to/plugin', [Host('host1'), Group('group1')])
