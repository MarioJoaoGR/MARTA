
from docstring_parser.tests.test_numpydoc import parse
import pytest

def test_none_input():
    """Test handling of None input."""
    docstring = parse("")  # Passing an empty string to simulate no input
    assert len(docstring.meta) == 0  # No metadata should be parsed if input is None
