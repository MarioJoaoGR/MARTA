
import pytest
from httpie.plugins.base import FormatterPlugin

def test_edge_case():
    # Create a mock Environment class for testing
    class MockEnvironment:
        pass
    
    env = MockEnvironment()
    format_options = {'style': 'pretty'}
    
    formatter = FormatterPlugin(env=env, format_options=format_options)
    
    assert formatter.enabled is True
    assert formatter.format_options == format_options
