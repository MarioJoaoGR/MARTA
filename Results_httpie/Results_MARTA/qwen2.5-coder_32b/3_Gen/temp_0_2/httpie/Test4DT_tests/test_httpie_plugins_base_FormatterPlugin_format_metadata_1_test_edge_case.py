
import pytest
from httpie.plugins.base import FormatterPlugin

def test_edge_case():
    # Create a mock Environment class for testing
    class MockEnvironment:
        pass
    
    # Instantiate the FormatterPlugin with a mock environment and format options
    formatter = FormatterPlugin(env=MockEnvironment(), format_options={'style': 'pretty'})
    
    # Test the edge case where metadata is just a string
    metadata = "Some metadata text"
    formatted_metadata = formatter.format_metadata(metadata)
    
    assert formatted_metadata == metadata, f"Expected {metadata}, but got {formatted_metadata}"
