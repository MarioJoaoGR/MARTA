
# Module: ansible.plugins.loader
# test_plugin_load_context.py
from ansible.plugins.loader import PluginLoadContext
import pytest

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_initialization(plugin_load_context):
    assert plugin_load_context.original_name is None
    assert plugin_load_context.redirect_list == []
    assert plugin_load_context.error_list == []
    assert plugin_load_context.import_error_list == []
    assert plugin_load_context.load_attempts == []
    assert plugin_load_context.pending_redirect is None
    assert plugin_load_context.exit_reason is None
    assert plugin_load_context.plugin_resolved_path is None
    assert plugin_load_context.plugin_resolved_name is None