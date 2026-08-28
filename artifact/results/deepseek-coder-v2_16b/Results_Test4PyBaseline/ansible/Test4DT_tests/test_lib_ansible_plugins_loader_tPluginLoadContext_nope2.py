
# Module: ansible.plugins.loader
# test_plugin_load_context.py
from ansible.plugins.loader import PluginLoadContext
import pytest

@pytest.fixture
def plugin_context():
    return PluginLoadContext()

def test_initialization(plugin_context):
    assert plugin_context.original_name is None
    assert plugin_context.redirect_list == []
    assert plugin_context.error_list == []
    assert plugin_context.import_error_list == []
    assert plugin_context.load_attempts == []
    assert plugin_context.pending_redirect is None
    assert plugin_context.exit_reason is None
    assert plugin_context.plugin_resolved_path is None
    assert plugin_context.plugin_resolved_name is None