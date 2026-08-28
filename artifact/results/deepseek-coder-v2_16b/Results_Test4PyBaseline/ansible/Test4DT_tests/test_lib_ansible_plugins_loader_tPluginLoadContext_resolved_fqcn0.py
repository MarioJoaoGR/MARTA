
import pytest
from ansible.plugins.loader import PluginLoadContext

# Test cases for the resolved_fqcn method in PluginLoadContext class

def test_resolved_fqcn_not_resolved():
    load_context = PluginLoadContext()
    assert load_context.resolved_fqcn is None

def test_resolved_fqcn_with_valid_redirects():
    load_context = PluginLoadContext()
    load_context.original_name = 'example_plugin'
    load_context.redirect_list = ['new_example_plugin', 'ansible.example.new_example_plugin']
    assert load_context.resolved_fqcn == 'ansible.example.new_example_plugin'

def test_resolved_fqcn_with_invalid_redirect():
    load_context = PluginLoadContext()
    load_context.original_name = 'example_plugin'
    load_context.redirect_list = ['invalid_plugin']
    assert load_context.resolved_fqcn == 'invalid_plugin'

def test_resolved_fqcn_with_legacy_prefix():
    load_context = PluginLoadContext()
    load_context.original_name = 'example_plugin'
    load_context.redirect_list = ['ansible.legacy.example_plugin']
    assert load_context.resolved_fqcn == 'example_plugin'

def test_resolved_fqcn_with_collection():
    load_context = PluginLoadContext()
    load_context.original_name = 'example_plugin'
    load_context.redirect_list = ['new_example_plugin']
    load_context.plugin_resolved_collection = 'ansible.example'
    assert load_context.resolved_fqcn == 'ansible.example.new_example_plugin'

def test_resolved_fqcn_with_pre_set_resolved():
    load_context = PluginLoadContext()
    load_context._resolved_fqcn = 'ansible.example.new_example_plugin'
    assert load_context.resolved_fqcn == 'ansible.example.new_example_plugin'
