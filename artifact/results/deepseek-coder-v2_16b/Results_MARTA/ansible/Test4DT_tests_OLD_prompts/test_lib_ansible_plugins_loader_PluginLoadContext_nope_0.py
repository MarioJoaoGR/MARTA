
import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoadContext


def test_nope_method():
    context = PluginLoadContext()
    with patch('ansible.plugins.loader.PluginLoadContext.__init__', lambda self: None):
        failed_context = context.nope(exit_reason='Plugin not found')
        assert failed_context.exit_reason == 'Plugin not found'
        assert not failed_context.resolved