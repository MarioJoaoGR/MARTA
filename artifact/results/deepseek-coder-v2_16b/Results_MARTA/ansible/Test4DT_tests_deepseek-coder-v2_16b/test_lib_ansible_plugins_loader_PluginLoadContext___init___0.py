
import pytest
from ansible.plugins.loader import PluginLoadContext

# Test initialization of PluginLoadContext

# Test redirection of PluginLoadContext
def test_PluginLoadContext_redirect():
    ctx = PluginLoadContext()
    redirected_ctx = ctx.redirect('new_plugin_name')
    assert redirected_ctx.pending_redirect == 'new_plugin_name'

# Test recording deprecation information in PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    ctx = PluginLoadContext()
    deprecation_info = {'warning_text': 'Use new_plugin instead.', 'removal_date': '2023-12-31'}
    ctx.record_deprecation('old_plugin', deprecation_info, 'my_collection')
    assert ctx.deprecated is True

# Test resolving the fully qualified class name in PluginLoadContext
def test_PluginLoadContext_resolve():
    ctx = PluginLoadContext()
    resolved_ctx = ctx.resolve('resolved_name', 'resolved_path', 'resolved_collection', 'resolved successfully')
    assert resolved_ctx.plugin_resolved_name == 'resolved_name'
    assert resolved_ctx.plugin_resolved_path == 'resolved_path'
    assert resolved_ctx.plugin_resolved_collection == 'resolved_collection'