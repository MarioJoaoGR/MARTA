
import pytest
from ansible.plugins.loader import PluginLoadContext

def test_resolve_with_valid_inputs():
    ctx = PluginLoadContext()
    resolved_context = ctx.resolve(
        resolved_name="ansible.legacy.some_module",
        resolved_path="/path/to/plugin/file",
        resolved_collection="my_collection",
        exit_reason="Plugin found successfully"
    )
    
    assert resolved_context.plugin_resolved_name == "ansible.legacy.some_module"
    assert resolved_context.plugin_resolved_path == "/path/to/plugin/file"
    assert resolved_context.plugin_resolved_collection == "my_collection"
    assert resolved_context.resolved is True
