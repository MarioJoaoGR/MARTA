
import pytest
from lib.ansible.plugins.loader import PluginPathContext

def test_valid_input():
    context = PluginPathContext(path='/internal/plugins/example', internal=True)
    assert context.path == '/internal/plugins/example'
    assert context.internal is True
