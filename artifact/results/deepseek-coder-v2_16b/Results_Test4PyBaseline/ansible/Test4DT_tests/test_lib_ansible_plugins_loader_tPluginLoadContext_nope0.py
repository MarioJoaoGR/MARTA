
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
    assert plugin_context.plugin_resolved_collection == ""
    assert not plugin_context.deprecated
    assert plugin_context.removal_date is None
    assert plugin_context.removal_version is None
    assert plugin_context.deprecation_warnings == []
    assert not plugin_context.resolved
    assert plugin_context._resolved_fqcn is None

def test_setting_original_name(plugin_context):
    plugin_context.original_name = 'example_plugin'
    assert plugin_context.original_name == 'example_plugin'

def test_adding_to_redirect_list(plugin_context):
    plugin_context.redirect_list.append('new_example_plugin')
    assert 'new_example_plugin' in plugin_context.redirect_list

def test_resolving_the_plugin(plugin_context):
    resolved_context = plugin_context.resolve(resolved_name="new_plugin_name", resolved_path="path/to/plugin", resolved_collection="", exit_reason="success")
    assert resolved_context.plugin_resolved_name == "new_plugin_name"
    assert resolved_context.plugin_resolved_path == "path/to/plugin"
    assert resolved_context.plugin_resolved_collection == ""
    assert resolved_context.exit_reason == "success"
    assert resolved_context.resolved

def test_redirecting_the_plugin(plugin_context):
    redirected_context = plugin_context.redirect('another_plugin')
    assert redirected_context.pending_redirect == 'another_plugin'

def test_setting_exit_reason_and_marking_as_unresolved(plugin_context):
    nope_context = plugin_context.nope("Plugin not found")
    assert nope_context.exit_reason == "Plugin not found"
    assert not nope_context.resolved

if __name__ == "__main__":
    pytest.main()
