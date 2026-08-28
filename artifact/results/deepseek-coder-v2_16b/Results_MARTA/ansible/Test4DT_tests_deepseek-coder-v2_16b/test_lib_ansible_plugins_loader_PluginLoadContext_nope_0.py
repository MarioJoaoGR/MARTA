
import pytest
from ansible.plugins.loader import PluginLoadContext

# Test scenarios
def test_valid_input():
    context = PluginLoadContext()
    context.original_name = 'some_plugin'
    failed_context = context.nope(exit_reason='Plugin not found')
    
    assert failed_context.exit_reason == 'Plugin not found'
    assert not failed_context.resolved

def test_edge_case_none():
    context = PluginLoadContext()
    context.original_name = 'some_plugin'
    failed_context = context.nope(exit_reason=None)
    
    assert failed_context.exit_reason is None
    assert not failed_context.resolved

def test_invalid_input():
    context = PluginLoadContext()
    context.original_name = 'some_plugin'
    failed_context = context.nope(exit_reason='')
    
    assert failed_context.exit_reason == ''
    assert not failed_context.resolved
