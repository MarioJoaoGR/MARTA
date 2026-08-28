
import pytest
from ansible.plugins.loader import PluginLoadContext

def test_no_deprecation():
    context = PluginLoadContext()
    deprecation_info = {'warning_text': 'Use new_plugin instead.', 'removal_date': '2023-12-31'}
    context.record_deprecation('old_plugin', deprecation_info, 'my_collection')
    assert hasattr(context, 'deprecation_warnings')
    assert len(context.deprecation_warnings) == 1
    assert "old_plugin has been deprecated." in context.deprecation_warnings[0]
