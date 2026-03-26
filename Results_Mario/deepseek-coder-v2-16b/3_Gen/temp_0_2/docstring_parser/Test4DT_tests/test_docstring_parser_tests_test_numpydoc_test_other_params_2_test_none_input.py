
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_none_input():
    """Test function behavior with None input."""
    # Call the function with None input
    docstring = parse(None)
    
    # Assert that there are no metadata entries
    assert len(docstring.meta) == 0
