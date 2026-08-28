
import pytest
from ansible.plugins.loader import PluginLoadContext

# Test cases for the resolved_fqcn method in the PluginLoadContext class

def test_resolved_fqcn_not_initialized():
    load_context = PluginLoadContext()
    assert load_context.resolved_fqcn is None

def test_resolved_fqcn_with_valid_redirects():
    load_context = PluginLoadContext()
    load_context.original_name = 'example_plugin'
    load_context.redirect_list = ['new_example_plugin', 'ansible.example.new_example_plugin']