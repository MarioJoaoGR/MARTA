
import pytest
from ansible.plugins.loader import PluginPathContext

def test_default_internal_status():
    context = PluginPathContext(path='/default/plugin/path', internal=False)
    assert hasattr(context, 'path')
    assert hasattr(context, 'internal')
    assert context.path == '/default/plugin/path'
    assert not context.internal

