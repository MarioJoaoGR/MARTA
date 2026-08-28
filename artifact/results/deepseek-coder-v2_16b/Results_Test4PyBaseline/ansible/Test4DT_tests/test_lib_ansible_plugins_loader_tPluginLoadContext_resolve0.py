# Module: ansible.plugins.loader
import pytest
from ansible.plugins.loader import PluginLoadContext

# Test case to check if the resolve method sets the correct properties
def test_resolve():
    load_context = PluginLoadContext()
    resolved_context = load_context.resolve(resolved_name="new_plugin_name", 
                                             resolved_path="path/to/plugin", 
                                             resolved_collection="", 
                                             exit_reason="success")
    assert resolved_context.plugin_resolved_name == "new_plugin_name"
    assert resolved_context.plugin_resolved_path == "path/to/plugin"
    assert resolved_context.plugin_resolved_collection == ""
    assert resolved_context.exit_reason == "success"
    assert resolved_context.resolved is True

# Test case to check if the redirect method sets the pending_redirect property correctly
def test_redirect():
    load_context = PluginLoadContext()
    redirected_context = load_context.redirect('another_plugin')
    assert redirected_context.pending_redirect == "another_plugin"

# Test case to check if the nope method sets the exit_reason property correctly
def test_nope():
    load_context = PluginLoadContext()
    nope_context = load_context.nope("Plugin not found")
    assert nope_context.exit_reason == "Plugin not found"
