
import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoadContext

def test_edge_case():
    with patch('ansible.plugins.loader.PluginLoadContext.__init__', return_value=None):
        ctx = PluginLoadContext()
        ctx.original_name = 'example_plugin'
        redirected_ctx = ctx.redirect(None)
        assert redirected_ctx.pending_redirect is None
        assert redirected_ctx.exit_reason == 'pending redirect resolution from example_plugin to None'
