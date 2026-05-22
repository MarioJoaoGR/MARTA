
import pytest
from httpie.plugins.base import FormatterPlugin
from unittest.mock import patch, MagicMock

def test_valid_input():
    # Create a mock Environment and format options
    env = MagicMock()
    format_options = {'style': 'pretty'}
    
    # Instantiate the FormatterPlugin with the mock environment and format options
    formatter = FormatterPlugin(env=env, format_options=format_options)
    
    # Test the format_metadata method
    metadata = "Some metadata text"
    formatted_metadata = formatter.format_metadata(metadata)
    
    # Assert that the output is the same as the input (no processing done yet)
    assert formatted_metadata == metadata
