
import pytest
from ansible.plugins.loader import PluginLoadContext

def test_valid_input():
    context = PluginLoadContext()
    deprecation_info = {'warning_text': 'Use new_plugin instead.', 'removal_date': '2023-12-31'}
    context.record_deprecation('old_plugin', deprecation_info, 'my_collection')
    
    assert context.deprecated is True
    assert context.deprecation_warnings == ['old_plugin has been deprecated. Use new_plugin instead.']
    assert context.removal_date == '2023-12-31'

def test_edge_case():
    context = PluginLoadContext()
    context.record_deprecation('old_plugin', None, 'my_collection')
    
    assert not context.deprecated
    assert len(context.deprecation_warnings) == 0
    assert context.removal_date is None

def test_invalid_input():
    context = PluginLoadContext()
    deprecation_info = {}
    context.record_deprecation('old_plugin', deprecation_info, 'my_collection')
    
    assert not context.deprecated
    assert len(context.deprecation_warnings) == 0
    assert context.removal_date is None
