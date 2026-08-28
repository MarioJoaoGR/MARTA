
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

# Test case to check if the resolve method handles empty collection correctly
def test_resolve_empty_collection():
    load_context = PluginLoadContext()
    resolved_context = load_context.resolve(resolved_name="new_plugin_name", 
                                             resolved_path="path/to/plugin", 
                                             resolved_collection="", 
                                             exit_reason="success")
    assert resolved_context.plugin_resolved_collection == ""

# Test case to check if the resolve method handles non-empty collection correctly
def test_resolve_non_empty_collection():
    load_context = PluginLoadContext()
    resolved_context = load_context.resolve(resolved_name="new_plugin_name", 
                                             resolved_path="path/to/plugin", 
                                             resolved_collection="some_collection", 
                                             exit_reason="success")
    assert resolved_context.plugin_resolved_collection == "some_collection"

# Test case to check if the resolve method sets resolved property correctly
def test_resolve_sets_resolved():
    load_context = PluginLoadContext()
    resolved_context = load_context.resolve(resolved_name="new_plugin_name", 
                                             resolved_path="path/to/plugin", 
                                             resolved_collection="", 
                                             exit_reason="success")
    assert resolved_context.resolved is True

# Test case to check if the resolve method returns self correctly
def test_resolve_returns_self():
    load_context = PluginLoadContext()
    returned_context = load_context.resolve(resolved_name="new_plugin_name", 
                                             resolved_path="path/to/plugin", 
                                             resolved_collection="", 
                                             exit_reason="success")
    assert returned_context is load_context
