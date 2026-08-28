
import pytest
from ansible.plugins.loader import PluginLoadContext

# Test Scenario 1: Valid Input
def test_valid_input():
    ctx = PluginLoadContext()
    ctx.original_name = 'some_plugin'
    ctx.redirect_list = ['ansible.legacy.some_plugin']
    ctx.plugin_resolved_collection = 'my_collection'
    
    assert ctx.original_name == 'some_plugin'
    assert ctx.redirect_list == ['ansible.legacy.some_plugin']
    assert ctx.plugin_resolved_collection == 'my_collection'
    assert ctx.resolved_fqcn() == 'ansible.legacy.some_plugin'

# Test Scenario 2: Edge Case with None Input
def test_edge_case():
    ctx = PluginLoadContext()
    ctx.original_name = None
    ctx.redirect_list = []
    ctx.plugin_resolved_collection = None
    
    assert ctx.original_name is None
    assert ctx.redirect_list == []
    assert ctx.plugin_resolved_collection is None
    with pytest.raises(AttributeError):
        ctx.resolved_fqcn()

# Test Scenario 3: Invalid Input
def test_invalid_input():
    ctx = PluginLoadContext()
    ctx.original_name = ''
    ctx.redirect_list = []
    ctx.plugin_resolved_collection = ''
    
    assert ctx.original_name == ''
    assert ctx.redirect_list == []
    assert ctx.plugin_resolved_collection == ''
    with pytest.raises(AttributeError):
        ctx.resolved_fqcn()
