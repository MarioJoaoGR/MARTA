
import pytest
from ansible.plugins.loader import PluginLoadContext
from ansible.errors import AnsibleError

def test_redirect():
    ctx = PluginLoadContext()
    ctx.original_name = 'example_plugin'
    
    redirected_ctx = ctx.redirect('new_plugin_name')
    assert redirected_ctx.pending_redirect == 'new_plugin_name'
    assert redirected_ctx.exit_reason == 'pending redirect resolution from example_plugin to new_plugin_name'
    assert not redirected_ctx.resolved
